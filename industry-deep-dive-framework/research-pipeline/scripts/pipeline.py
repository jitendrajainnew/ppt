#!/usr/bin/env python3
"""
Research pipeline: Screener → document links → bulk download → text extraction → manifest.

Turns a list of NSE/BSE tickers into a local research database of annual reports,
concall transcripts, and investor presentations — extracted to plain text, ready to read.

Usage:
  python3 pipeline.py links  SUNPHARMA CIPLA DIVISLAB ...     # scrape doc links from Screener
  python3 pipeline.py fetch  SUNPHARMA ...                    # download prioritized subset
  python3 pipeline.py extract SUNPHARMA ...                   # PDF -> text
  python3 pipeline.py all    SUNPHARMA ...                    # links + fetch + extract
Env:
  MAX_AR=3 MAX_CALL=6 MAX_PPT=2   # how many of each doc type to keep per company
"""
import os, re, sys, json, time, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW, TXT = ROOT/"data"/"raw", ROOT/"data"/"text"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
MAX_AR  = int(os.environ.get("MAX_AR", 3))
MAX_CALL= int(os.environ.get("MAX_CALL", 6))
MAX_PPT = int(os.environ.get("MAX_PPT", 2))

def curl(url, out=None, timeout=60):
    cmd = ["curl","-sS","-L","--max-time",str(timeout),"-A",UA,
           "-H","Referer: https://www.screener.in/"]
    if out: cmd += ["-o", out, "-w", "%{http_code}"]
    try:
        r = subprocess.run(cmd+[url], capture_output=True, text=True, errors="ignore", timeout=timeout+10)
        return r.stdout if out is None else r.stdout.strip()
    except Exception as e:
        return f"ERR {e}"

def categorize(url):
    u = url.lower()
    if "annualreport" in u or "annual_report" in u or "/ar_" in u: return "annual_report"
    if any(k in u for k in ["transcript","earnings-call","concall","earnings_call"]): return "concall"
    if any(k in u for k in ["presentation","ir-presentation","investor","-ppt","/ppt"]): return "presentation"
    return "announcement"

def get_links(sym):
    """Scrape Screener consolidated + standalone page for document links, categorized + ordered."""
    links, seen = [], set()
    for variant in ("consolidated/","" ):
        html = curl(f"https://www.screener.in/company/{sym}/{variant}")
        if not isinstance(html,str) or len(html)<1000: continue
        for m in re.findall(r'href="(https?://[^"]+\.(?:pdf|zip))"', html, re.I):
            u = m.split("#")[0]
            if u in seen: continue
            seen.add(u); links.append({"url":u,"type":categorize(u)})
    # prioritize: annual reports, concalls, presentations (keep source order = newest-first on Screener)
    out = []
    for t,cap in (("annual_report",MAX_AR),("concall",MAX_CALL),("presentation",MAX_PPT)):
        out += [l for l in links if l["type"]==t][:cap]
    return out, links

def cmd_links(syms):
    idx = {}
    for s in syms:
        sel, alll = get_links(s)
        idx[s] = sel
        (RAW/s).mkdir(parents=True, exist_ok=True)
        json.dump({"selected":sel,"all":alll}, open(RAW/s/"_links.json","w"), indent=1)
        print(f"{s}: {len(alll)} docs found, {len(sel)} selected "
              f"({sum(d['type']=='annual_report' for d in sel)} AR, "
              f"{sum(d['type']=='concall' for d in sel)} calls, "
              f"{sum(d['type']=='presentation' for d in sel)} ppt)")
        time.sleep(1)
    return idx

def cmd_fetch(syms):
    man = []
    for s in syms:
        meta = json.load(open(RAW/s/"_links.json"))
        for i,d in enumerate(meta["selected"]):
            name = f"{d['type']}_{i:02d}.pdf"
            dst = RAW/s/name
            if dst.exists() and dst.stat().st_size>2000:
                man.append((s,name,"cached",d["url"])); continue
            code = curl(d["url"], str(dst))
            ok = dst.exists() and dst.stat().st_size>2000 and code=="200"
            man.append((s,name,"ok" if ok else f"FAIL {code}",d["url"]))
            print(f"{s}/{name}: {man[-1][2]} ({dst.stat().st_size if dst.exists() else 0} B)")
            time.sleep(0.6)
    json.dump(man, open(RAW/"_manifest.json","w"), indent=1)
    return man

def cmd_extract(syms):
    from pdfminer.high_level import extract_text
    for s in syms:
        (TXT/s).mkdir(parents=True, exist_ok=True)
        for pdf in sorted((RAW/s).glob("*.pdf")):
            out = TXT/s/(pdf.stem+".txt")
            if out.exists() and out.stat().st_size>500:
                print(f"{s}/{pdf.name}: cached"); continue
            try:
                t = extract_text(str(pdf)) or ""
                t = re.sub(r"\n{3,}","\n\n",t)
                out.write_text(t)
                print(f"{s}/{pdf.name}: {len(t)} chars")
            except Exception as e:
                print(f"{s}/{pdf.name}: ERR {e}")

if __name__=="__main__":
    if len(sys.argv)<3: print(__doc__); sys.exit(1)
    op, syms = sys.argv[1], [a.upper() for a in sys.argv[2:]]
    if op in ("links","all"):   cmd_links(syms)
    if op in ("fetch","all"):   cmd_fetch(syms)
    if op in ("extract","all"): cmd_extract(syms)
