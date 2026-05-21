import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv("data/balanced_data.csv")
# Features
X = df.drop("loan_default", axis=1)

# Target
y = df["loan_default"]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# Save processed data
joblib.dump(
    (X_train, X_test, y_train, y_test),
    "model_training/data.pkl"
)

# Save scaler
joblib.dump(
    scaler,
    "model_training/scaler.pkl"
)

print("Preprocessing Complete")
print("Training:", X_train.shape)
print("Testing:", X_test.shape)