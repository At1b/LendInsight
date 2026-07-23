import joblib

from models.forecasting import train_model

print("Training Random Forest model...")

model, metrics, X_test, y_test, y_pred, feature_names = train_model()

joblib.dump(
    {
        "model": model,
        "metrics": metrics,
        "feature_names": list(feature_names),
        "y_test": y_test,
        "y_pred": y_pred
    },
    "models/random_forest_model.pkl"
)

print("✅ Model saved successfully!")