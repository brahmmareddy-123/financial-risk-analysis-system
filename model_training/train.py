import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load processed data
X_train, X_test, y_train, y_test = joblib.load(
    "model_training/data.pkl"
)

models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}

best_model = None
best_accuracy = 0

for name, model in models.items():

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, pred)

    print(name, "Accuracy:", accuracy)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Save best model
joblib.dump(
    best_model,
    "model_training/model.pkl"
)

print("\nBest Accuracy:", best_accuracy)
print("Best Model Saved")