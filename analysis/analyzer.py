"""
Trade analysis and reporting module.
Generates statistics, visualizations, and Excel reports from parsed trades.
"""

import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import pandas as pd

import config


class TradeAnalyzer:
    """Analyzes parsed trade data and generates reports."""

    def __init__(self):
        self.trades_file = config.OUTPUT_DIR / "trades.json"
        self.report_file = config.OUTPUT_DIR / "trade_report.xlsx"
        self.stats_file = config.OUTPUT_DIR / "trade_stats.json"
        self.df = None

    def load_trades(self) -> pd.DataFrame:
        """Load trades from JSON into a DataFrame."""
        if not self.trades_file.exists():
            print("ERROR: No trades.json found. Run the parser first.")
            return pd.DataFrame()

        with open(self.trades_file, "r") as f:
            trades = json.load(f)

        if not trades:
            print("No trades found in trades.json")
            return pd.DataFrame()

        self.df = pd.DataFrame(trades)

        # Parse dates
        if "date" in self.df.columns:
            self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce")
            self.df["date_only"] = self.df["date"].dt.date
            self.df["hour"] = self.df["date"].dt.hour
            self.df["day_of_week"] = self.df["date"].dt.day_name()
            self.df["month"] = self.df["date"].dt.to_period("M").astype(str)

        print(f"Loaded {len(self.df)} trades")
        return self.df

    def compute_stats(self) -> dict:
        """Compute comprehensive trade statistics."""
        if self.df is None or self.df.empty:
            self.load_trades()
        if self.df is None or self.df.empty:
            return {}

        df = self.df
        stats = {}

        # ── Overview ──────────────────────────────────────────
        stats["total_trades"] = len(df)
        stats["date_range"] = {
            "from": str(df["date"].min()) if "date" in df.columns else "N/A",
            "to": str(df["date"].max()) if "date" in df.columns else "N/A",
        }

        # ── Trade types ──────────────────────────────────────
        stats["by_type"] = df["trade_type"].value_counts().to_dict()
        stats["by_instrument"] = df["instrument"].value_counts().to_dict()
        stats["by_symbol"] = df["symbol"].value_counts().head(10).to_dict()
        stats["by_status"] = df["status"].value_counts().to_dict()
        stats["by_source"] = df["source"].value_counts().to_dict()

        # ── P&L analysis ─────────────────────────────────────
        closed = df[df["pnl"] != 0]
        if not closed.empty:
            winners = closed[closed["pnl"] > 0]
            losers = closed[closed["pnl"] < 0]

            stats["pnl"] = {
                "total_closed_trades": len(closed),
                "total_pnl": round(float(closed["pnl"].sum()), 2),
                "average_pnl": round(float(closed["pnl"].mean()), 2),
                "median_pnl": round(float(closed["pnl"].median()), 2),
                "max_profit": round(float(closed["pnl"].max()), 2),
                "max_loss": round(float(closed["pnl"].min()), 2),
                "winners": len(winners),
                "losers": len(losers),
                "win_rate": round(len(winners) / len(closed) * 100, 1) if len(closed) > 0 else 0,
                "avg_winner": round(float(winners["pnl"].mean()), 2) if not winners.empty else 0,
                "avg_loser": round(float(losers["pnl"].mean()), 2) if not losers.empty else 0,
            }

            # Risk-reward ratio
            if stats["pnl"]["avg_loser"] != 0:
                stats["pnl"]["risk_reward_ratio"] = round(
                    abs(stats["pnl"]["avg_winner"] / stats["pnl"]["avg_loser"]), 2
                )
            else:
                stats["pnl"]["risk_reward_ratio"] = float("inf")
        else:
            stats["pnl"] = {"note": "No closed trades with P&L data"}

        # ── Time analysis ─────────────────────────────────────
        if "hour" in df.columns:
            stats["by_hour"] = df["hour"].value_counts().sort_index().to_dict()
        if "day_of_week" in df.columns:
            stats["by_day"] = df["day_of_week"].value_counts().to_dict()
        if "month" in df.columns:
            stats["by_month"] = df["month"].value_counts().sort_index().to_dict()

        # ── Confidence distribution ──────────────────────────
        if "confidence" in df.columns:
            stats["confidence"] = {
                "mean": round(float(df["confidence"].mean()), 2),
                "high_confidence_count": int((df["confidence"] >= 0.5).sum()),
                "low_confidence_count": int((df["confidence"] < 0.3).sum()),
            }

        # ── Streaks ──────────────────────────────────────────
        if not closed.empty:
            wins_losses = (closed["pnl"] > 0).astype(int).tolist()
            stats["streaks"] = {
                "max_win_streak": self._max_streak(wins_losses, 1),
                "max_loss_streak": self._max_streak(wins_losses, 0),
            }

        # Save stats
        with open(self.stats_file, "w") as f:
            json.dump(stats, f, indent=2, default=str)

        print(f"Stats saved to: {self.stats_file}")
        return stats

    def generate_excel_report(self):
        """Generate a comprehensive Excel report with multiple sheets."""
        if self.df is None or self.df.empty:
            self.load_trades()
        if self.df is None or self.df.empty:
            return

        stats = self.compute_stats()

        with pd.ExcelWriter(self.report_file, engine="openpyxl") as writer:
            # Sheet 1: All trades
            df_export = self.df.drop(columns=["raw_text", "tags"], errors="ignore")
            df_export.to_excel(writer, sheet_name="All Trades", index=False)

            # Sheet 2: Summary stats
            summary_rows = [
                ("Total Trades", stats.get("total_trades", 0)),
                ("Date Range From", stats.get("date_range", {}).get("from", "")),
                ("Date Range To", stats.get("date_range", {}).get("to", "")),
            ]
            pnl = stats.get("pnl", {})
            if "total_pnl" in pnl:
                summary_rows.extend([
                    ("", ""),
                    ("-- P&L Summary --", ""),
                    ("Total Closed Trades", pnl.get("total_closed_trades", 0)),
                    ("Total P&L", pnl.get("total_pnl", 0)),
                    ("Average P&L", pnl.get("average_pnl", 0)),
                    ("Max Profit", pnl.get("max_profit", 0)),
                    ("Max Loss", pnl.get("max_loss", 0)),
                    ("Win Rate %", pnl.get("win_rate", 0)),
                    ("Risk Reward Ratio", pnl.get("risk_reward_ratio", 0)),
                    ("Winners", pnl.get("winners", 0)),
                    ("Losers", pnl.get("losers", 0)),
                    ("Avg Winner", pnl.get("avg_winner", 0)),
                    ("Avg Loser", pnl.get("avg_loser", 0)),
                ])

            pd.DataFrame(summary_rows, columns=["Metric", "Value"]).to_excel(
                writer, sheet_name="Summary", index=False
            )

            # Sheet 3: By Symbol
            if "by_symbol" in stats:
                pd.DataFrame(
                    list(stats["by_symbol"].items()), columns=["Symbol", "Count"]
                ).to_excel(writer, sheet_name="By Symbol", index=False)

            # Sheet 4: By Month
            if "by_month" in stats:
                pd.DataFrame(
                    list(stats["by_month"].items()), columns=["Month", "Count"]
                ).to_excel(writer, sheet_name="By Month", index=False)

            # Sheet 5: Monthly P&L
            if "date" in self.df.columns and "pnl" in self.df.columns:
                closed = self.df[self.df["pnl"] != 0].copy()
                if not closed.empty and "month" in closed.columns:
                    monthly = closed.groupby("month").agg(
                        trades=("pnl", "count"),
                        total_pnl=("pnl", "sum"),
                        avg_pnl=("pnl", "mean"),
                        win_rate=("pnl", lambda x: round((x > 0).sum() / len(x) * 100, 1)),
                    ).reset_index()
                    monthly.to_excel(writer, sheet_name="Monthly P&L", index=False)

        print(f"Excel report saved to: {self.report_file}")

    def generate_charts(self):
        """Generate visualization charts and save as images."""
        if self.df is None or self.df.empty:
            self.load_trades()
        if self.df is None or self.df.empty:
            return

        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        charts_dir = config.OUTPUT_DIR / "charts"
        charts_dir.mkdir(exist_ok=True)

        closed = self.df[self.df["pnl"] != 0].copy()

        # 1. Cumulative P&L over time
        if not closed.empty and "date" in closed.columns:
            fig, ax = plt.subplots(figsize=(12, 6))
            sorted_df = closed.sort_values("date")
            sorted_df["cumulative_pnl"] = sorted_df["pnl"].cumsum()
            ax.plot(sorted_df["date"], sorted_df["cumulative_pnl"], linewidth=2)
            ax.set_title("Cumulative P&L Over Time")
            ax.set_xlabel("Date")
            ax.set_ylabel("Cumulative P&L (points)")
            ax.axhline(y=0, color="red", linestyle="--", alpha=0.5)
            ax.grid(True, alpha=0.3)
            fig.tight_layout()
            fig.savefig(charts_dir / "cumulative_pnl.png", dpi=150)
            plt.close(fig)
            print(f"  Saved: cumulative_pnl.png")

        # 2. Win rate pie chart
        if not closed.empty:
            fig, ax = plt.subplots(figsize=(8, 8))
            winners = (closed["pnl"] > 0).sum()
            losers = (closed["pnl"] <= 0).sum()
            ax.pie(
                [winners, losers],
                labels=[f"Winners ({winners})", f"Losers ({losers})"],
                colors=["#2ecc71", "#e74c3c"],
                autopct="%1.1f%%",
                startangle=90,
                textprops={"fontsize": 14},
            )
            ax.set_title("Win Rate", fontsize=16)
            fig.tight_layout()
            fig.savefig(charts_dir / "win_rate.png", dpi=150)
            plt.close(fig)
            print(f"  Saved: win_rate.png")

        # 3. P&L distribution
        if not closed.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(closed["pnl"], bins=30, color="#3498db", edgecolor="white", alpha=0.8)
            ax.axvline(x=0, color="red", linestyle="--", alpha=0.7)
            ax.set_title("P&L Distribution")
            ax.set_xlabel("P&L (points)")
            ax.set_ylabel("Frequency")
            ax.grid(True, alpha=0.3)
            fig.tight_layout()
            fig.savefig(charts_dir / "pnl_distribution.png", dpi=150)
            plt.close(fig)
            print(f"  Saved: pnl_distribution.png")

        # 4. Trades by symbol
        if "symbol" in self.df.columns:
            symbol_counts = self.df["symbol"].value_counts().head(10)
            if not symbol_counts.empty:
                fig, ax = plt.subplots(figsize=(10, 6))
                symbol_counts.plot(kind="barh", ax=ax, color="#9b59b6")
                ax.set_title("Most Traded Symbols")
                ax.set_xlabel("Number of Trades")
                ax.grid(True, alpha=0.3, axis="x")
                fig.tight_layout()
                fig.savefig(charts_dir / "by_symbol.png", dpi=150)
                plt.close(fig)
                print(f"  Saved: by_symbol.png")

        # 5. Trades by hour of day
        if "hour" in self.df.columns:
            fig, ax = plt.subplots(figsize=(10, 6))
            hour_counts = self.df["hour"].value_counts().sort_index()
            ax.bar(hour_counts.index, hour_counts.values, color="#e67e22")
            ax.set_title("Trades by Hour of Day")
            ax.set_xlabel("Hour")
            ax.set_ylabel("Number of Trades")
            ax.set_xticks(range(0, 24))
            ax.grid(True, alpha=0.3, axis="y")
            fig.tight_layout()
            fig.savefig(charts_dir / "by_hour.png", dpi=150)
            plt.close(fig)
            print(f"  Saved: by_hour.png")

        # 6. Monthly P&L bar chart
        if not closed.empty and "month" in closed.columns:
            fig, ax = plt.subplots(figsize=(12, 6))
            monthly_pnl = closed.groupby("month")["pnl"].sum()
            colors = ["#2ecc71" if v >= 0 else "#e74c3c" for v in monthly_pnl.values]
            monthly_pnl.plot(kind="bar", ax=ax, color=colors)
            ax.set_title("Monthly P&L")
            ax.set_xlabel("Month")
            ax.set_ylabel("Total P&L (points)")
            ax.axhline(y=0, color="black", linestyle="-", linewidth=0.5)
            ax.grid(True, alpha=0.3, axis="y")
            fig.tight_layout()
            fig.savefig(charts_dir / "monthly_pnl.png", dpi=150)
            plt.close(fig)
            print(f"  Saved: monthly_pnl.png")

        print(f"\nAll charts saved to: {charts_dir}")

    def print_summary(self):
        """Print a human-readable summary to the console."""
        stats = self.compute_stats()
        if not stats:
            return

        print("\n" + "=" * 60)
        print("  TRADE ANALYSIS SUMMARY")
        print("=" * 60)

        print(f"\n  Total trades parsed: {stats['total_trades']}")
        dr = stats.get("date_range", {})
        print(f"  Date range: {dr.get('from', 'N/A')} to {dr.get('to', 'N/A')}")

        print(f"\n  By type: {stats.get('by_type', {})}")
        print(f"  By instrument: {stats.get('by_instrument', {})}")
        print(f"  Top symbols: {stats.get('by_symbol', {})}")

        pnl = stats.get("pnl", {})
        if "total_pnl" in pnl:
            print(f"\n  --- P&L Analysis ---")
            print(f"  Closed trades: {pnl['total_closed_trades']}")
            print(f"  Total P&L:     {pnl['total_pnl']:+.2f}")
            print(f"  Win rate:      {pnl['win_rate']}%")
            print(f"  Avg winner:    {pnl['avg_winner']:+.2f}")
            print(f"  Avg loser:     {pnl['avg_loser']:+.2f}")
            print(f"  Risk/Reward:   {pnl['risk_reward_ratio']}")
            print(f"  Max profit:    {pnl['max_profit']:+.2f}")
            print(f"  Max loss:      {pnl['max_loss']:+.2f}")

        streaks = stats.get("streaks", {})
        if streaks:
            print(f"\n  Max win streak:  {streaks.get('max_win_streak', 0)}")
            print(f"  Max loss streak: {streaks.get('max_loss_streak', 0)}")

        print("\n" + "=" * 60)

    @staticmethod
    def _max_streak(values: list, target: int) -> int:
        """Calculate maximum consecutive streak of target value."""
        max_s = 0
        current = 0
        for v in values:
            if v == target:
                current += 1
                max_s = max(max_s, current)
            else:
                current = 0
        return max_s
