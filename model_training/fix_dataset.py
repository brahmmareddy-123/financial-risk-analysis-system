import pandas as pd
import numpy as np

df = pd.read_csv("data/Financial Risk Classification Dataset.csv")

# Create realistic loan default labels
df["loan_default"] = np.where(
    (
        (df["credit_score"] < 500) |
        (df["annual_income"] < 25000) |
        (df["previous_default_count"] > 2) |
        (df["debt_to_income_ratio"] > 0.6)
    ),
    1,
    0
)

df.to_csv("data/balanced_data.csv", index=False)

print(df["loan_default"].value_counts())
print("Balanced dataset created")