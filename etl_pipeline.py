import pandas as pd

# 1. Read the raw CSV, skipping row 0 (the report title banner)
raw_file = "MD CC Transfer Students by USM Institutions.csv"
df = pd.read_csv(raw_file, skiprows=1)

# 2. Rename columns cleanly
df.columns = [
    "institution",
    "fy_2022",
    "fy_2023",
    "fy_2024",
    "fy_2025",
    "fy_2026",
    "yoy_change_pct",
    "avg_annual_change_pct",
]

# 3. Remove the 'Total' summary row and bottom 'Note:' row
df = df[~df["institution"].str.startswith(("Total", "Note:"), na=True)].copy()
df["institution"] = df["institution"].str.strip()

# 4. Clean commas and '%' signs so numbers are stored properly
fy_cols = ["fy_2022", "fy_2023", "fy_2024", "fy_2025", "fy_2026"]
for col in fy_cols:
    df[col] = df[col].astype(str).str.replace(",", "", regex=False).astype(int)

for col in ["yoy_change_pct", "avg_annual_change_pct"]:
    df[col] = df[col].astype(str).str.replace("%", "", regex=False).astype(float)

# 5. Reshape from wide table to normalized long format for SQL/PostgreSQL
df_long = df.melt(
    id_vars=["institution"],
    value_vars=fy_cols,
    var_name="fiscal_year",
    value_name="transfer_students",
)
df_long["fiscal_year"] = df_long["fiscal_year"].str.replace("fy_", "", regex=False).astype(int)

# 6. Save both cleaned files
df.to_csv("usm_transfers_wide_clean.csv", index=False)
df_long.to_csv("usm_transfers_normalized_long.csv", index=False)

print("Success! Cleaned files created:")
print(df.head())