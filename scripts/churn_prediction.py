import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

CLEANED_PATH = "data/churn_cleaned.csv"

def main():
    try:
        df = pd.read_csv(CLEANED_PATH)
    except FileNotFoundError:
        print("Run data Cleaning file")
        return
    # Use numeric/categorical columns
    cat_cols = ["Contract", "PaymentMethod", "InternetService", "TenureBucket"]
    num_cols = [c for c in ["tenure", "Tenure", "MonthlyCharges", "TotalCharges"] if c in df.columns]

    X = df[num_cols].copy()
    for col in cat_cols:
        if col in df.columns:
            le = LabelEncoder()
            X[col] = le.fit_transform(df[col].astype(str).fillna(""))
    y = df["ChurnFlag"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("Accuracy:", round(accuracy_score(y_test, preds), 4))
    print(classification_report(y_test, preds, target_names=["No Churn", "Churn"]))

if __name__ == "__main__":
    main()
