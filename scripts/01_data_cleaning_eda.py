"""
Customer Churn Analysis — Data Cleaning & EDA
Day 1–2: Load, clean, segment, and export for Power BI.
Dataset: Telco Customer Churn (e.g. Kaggle WA_Fn-UseC_-Telco-Customer-Churn.csv)
Run from project root: python scripts/01_data_cleaning_eda.py
"""

import pandas as pd
import numpy as np

# Paths (run from project root)
RAW_PATH = "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"  # Kaggle default name
CLEANED_PATH = "data/churn_cleaned.csv"

def load_data():
    """Load raw churn CSV. Place your file in data/ folder."""
    try:
        return pd.read_csv(RAW_PATH)
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Put the Telco Churn CSV in the 'data/' folder as: {RAW_PATH}\n"
            "Download: https://www.kaggle.com/datasets/blastchar/telco-customer-churn"
        )

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values, duplicates, and create churn flag."""
    df = df.copy()

    # TotalCharges is often stored as object with empty strings for new customers
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Drop rows with missing critical columns (or impute: e.g. TotalCharges = 0 for tenure 0)
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    if len(df) < before:
        print(f"  Removed {before - len(df)} duplicate rows.")

    # Ensure churn flag exists (Yes/No or 1/0)
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
    print("Loading data...")
    df = load_data()
    print("Cleaning...")
    df = clean_data(df)
    print("Adding segments...")
    df = add_segments(df)
    run_eda_summary(df)

    df.to_csv(CLEANED_PATH, index=False)
    print(f"Saved cleaned data to: {CLEANED_PATH}")
    print("Use this file in Power BI for your dashboard.")

if __name__ == "__main__":
    main()
