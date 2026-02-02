import pandas as pd

RAW_PATH = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv" 
CLEANED_PATH = "data/churn_cleaned.csv"

def load_data():
    """Load data"""
    try:
        return pd.read_csv(RAW_PATH)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Put the churn file"
        )

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values, duplicates."""
    df = df.copy()

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    if len(df) < before:
        print(f"  Removed {before - len(df)} duplicate rows.")

    # Ensure churn flag exists
    if "Churn" not in df.columns:
        raise ValueError("Dataset must have a 'Churn' column.")
    df["ChurnFlag"] = (df["Churn"].astype(str).str.strip().str.lower() == "yes").astype(int)

    return df

def add_segments(df: pd.DataFrame) -> pd.DataFrame:
    """Segment customers by tenure and spend for dashboard."""
    df = df.copy()

    # Tenure buckets (months)
    def tenure_bucket(t):
        if pd.isna(t) or t < 0:
            return "Unknown"
        if t <= 6:
            return "0-6 months"
        if t <= 12:
            return "7-12 months"
        if t <= 24:
            return "13-24 months"
        return "24+ months"

    tenure_col = "tenure" if "tenure" in df.columns else "Tenure"
    df["TenureBucket"] = df[tenure_col].apply(tenure_bucket)

    # Spend segment (monthly charges)
    if "MonthlyCharges" in df.columns:
        df["SpendSegment"] = pd.cut(
            df["MonthlyCharges"],
            bins=[0, 35, 70, 105, 200],
            labels=["Low (0-35)", "Medium (35-70)", "High (70-105)", "Very High (105+)"],
        ).astype(str)

    return df

def run_eda_summary(df: pd.DataFrame) -> None:
    """Print basic EDA summary to console."""
    print("\n--- EDA Summary ---")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Churn rate: {df['ChurnFlag'].mean():.2%}")
    if "TenureBucket" in df.columns:
        print("\nChurn by tenure bucket:")
        print(df.groupby("TenureBucket", sort=False)["ChurnFlag"].agg(["mean", "count"]).round(4))
    if "Contract" in df.columns:
        print("\nChurn by contract:")
        print(df.groupby("Contract")["ChurnFlag"].mean().sort_values(ascending=False))
    print()

def main():
    df = load_data()
    df = clean_data(df)
    df = add_segments(df)
    run_eda_summary(df)

    df.to_csv(CLEANED_PATH, index=False)

if __name__ == "__main__":
    main()
