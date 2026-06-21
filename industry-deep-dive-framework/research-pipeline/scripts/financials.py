#!/usr/bin/env python3
"""
Pull clean 10-year financials from Screener's structured HTML tables (not OCR'd PDFs).
Far more reliable than parsing annual-report PDFs for the long-run series.

Usage: python3 financials.py SUNPHARMA CIPLA DIVISLAB DRREDDY MANKIND TORNTPHARM
Writes: data/financials/<TICKER>.json  and prints a compact table.
"""
import sys, re, json, html, subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT/"data"/"financials"; OUT.mkdir(parents=True, exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"

def fetch(sym):
    for v in ("consolidated/",""):
        r = subprocess.run(["curl","-sS","-L","--max-time","30","-A",UA,
                            "-H","Referer: https://www.screener.in/",
                            f"https://www.screener.in/company/{sym}/{v}"],
                           capture_output=True, text=True, errors="ignore", timeout=40)
        if r.stdout and len(r.stdout) > 5000:
            return r.stdout
    return ""

def parse_section(t, sec_id):
    m = re.search(r'id="'+sec_id+r'".*?</section>', t, re.S)
    seg = m.group(0) if m else ""
    yrs = re.findall(r'<th[^>]*>\s*([A-Za-z]{3}\s*20\d{2}|TTM)\s*</th>', seg)
    rows = {}
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', seg, re.S):
        name = re.search(r'<td[^>]*class="[^"]*text[^"]*"[^>]*>(.*?)</td>', tr, re.S)
        if not name: continue
        nm = re.sub(r'<[^>]+>','',name.group(1))
        nm = html.unescape(nm).replace('\xa0',' ').strip().strip('+').strip()
        vals = re.findall(r'<td[^>]*class="">\s*([-0-9,\.%]*)\s*</td>', tr)
        if not vals:
            vals = [re.sub(r'<[^>]+>','',x).strip() for x in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)][1:]
        vals = [v.replace(',','').strip() for v in vals]
        if nm and any(v for v in vals): rows[nm] = vals
    return yrs, rows

def main(syms):
    for s in syms:
        t = fetch(s)
        if not t: print(f"{s}: FETCH FAIL"); continue
        pl_yrs, pl = parse_section(t, "profit-loss")
        rt_yrs, rt = parse_section(t, "ratios")
        data = {"years_pl": pl_yrs, "pl": pl, "years_ratios": rt_yrs, "ratios": rt}
        json.dump(data, open(OUT/f"{s}.json","w"), indent=1)
        def row(d, *keys):
            for k in keys:
                for nm,v in d.items():
                    if k.lower() in nm.lower(): return nm, v
            return None, None
        print(f"\n===== {s} =====  years: {pl_yrs}")
        for label,keys in [("Sales",["Sales","Revenue"]),("OPM%",["OPM"]),
                           ("Net Profit",["Net Profit"]),("EPS",["EPS"])]:
            nm,v = row(pl, *keys);  print(f"  {label:11s}: {v}")
        for label,keys in [("ROCE%",["ROCE"]),("ROE%",["Return on equity","ROE"])]:
            nm,v = row(rt, *keys);  print(f"  {label:11s}: {v}")

if __name__=="__main__":
    main([a.upper() for a in sys.argv[1:]] or ["SUNPHARMA"])
