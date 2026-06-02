import os
import pandas as pd

RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "data", "raw")
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

FUND_MASTER_FILE = os.path.join(RAW_DATA_DIR, "fund_master.csv")
NAV_HISTORY_FILE = os.path.join(RAW_DATA_DIR, "nav_history.csv")

os.makedirs(REPORTS_DIR, exist_ok=True)


def main():
    print("\nMUTUAL FUND ANALYSIS - Day 1: AMFI Code Validation\n")

    if not os.path.exists(FUND_MASTER_FILE):
        print("fund_master.csv not found")
        return

    if not os.path.exists(NAV_HISTORY_FILE):
        print("nav_history.csv not found")
        return

    fund_master = pd.read_csv(FUND_MASTER_FILE)
    nav_history = pd.read_csv(NAV_HISTORY_FILE)

    print(f"Loaded fund_master: {fund_master.shape}")
    print(f"Loaded nav_history: {nav_history.shape}")

    # Find AMFI code column
    fm_code_col = None
    nh_code_col = None

    for col in fund_master.columns:
        if "amfi" in col.lower() or "scheme" in col.lower():
            fm_code_col = col
            break

    for col in nav_history.columns:
        if "amfi" in col.lower() or "scheme" in col.lower():
            nh_code_col = col
            break

    if fm_code_col is None or nh_code_col is None:
        print("\nCould not find AMFI/Scheme Code columns.")
        print("Fund Master Columns:", list(fund_master.columns))
        print("NAV History Columns:", list(nav_history.columns))
        return

    fm_codes = set(fund_master[fm_code_col].dropna())
    nh_codes = set(nav_history[nh_code_col].dropna())

    missing_in_nav = fm_codes - nh_codes
    extra_in_nav = nh_codes - fm_codes

    print("\nDATA QUALITY SUMMARY")
    print("-" * 40)

    print(f"Codes in fund_master : {len(fm_codes)}")
    print(f"Codes in nav_history : {len(nh_codes)}")
    print(f"Codes in both files  : {len(fm_codes & nh_codes)}")

    print(f"\nMissing in nav_history : {len(missing_in_nav)}")
    print(f"Extra in nav_history   : {len(extra_in_nav)}")

    report_path = os.path.join(REPORTS_DIR, "data_quality_summary.txt")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("DATA QUALITY SUMMARY\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Codes in fund_master : {len(fm_codes)}\n")
        f.write(f"Codes in nav_history : {len(nh_codes)}\n")
        f.write(f"Codes in both files  : {len(fm_codes & nh_codes)}\n\n")
        f.write(f"Missing in nav_history : {len(missing_in_nav)}\n")
        f.write(f"Extra in nav_history   : {len(extra_in_nav)}\n")

    print(f"\nReport saved: {report_path}")
    print("\nValidation completed successfully.")

if __name__ == "__main__":
    main()