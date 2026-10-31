
import joblib
import sklearn
from pathlib import Path

model_path = Path(
    "models/PulmoLens_Calibrated_Model.joblib"
)

print("Checking PulmoLens model...")

if not model_path.exists():
    raise FileNotFoundError(
        "Calibrated model file is missing!"
    )

model = joblib.load(model_path)

print("\nMODEL LOADED SUCCESSFULLY!")

print("Scikit-learn version:", sklearn.__version__)
print("Model type:", type(model))
print("Classes:", model.classes_)
print("Input features:", model.n_features_in_)

print("\nPulmoLens model integration test passed!")
