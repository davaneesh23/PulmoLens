
from utils.prediction import predict_respiratory_probability

# Example NHANES-style research record
sample_participant = {
    "RIDAGEYR": 45,
    "RIAGENDR": 1.0,
    "RIDRETH1": 3.0,
    "DMDEDUC2": 4.0,
    "DMDMARTL": 1.0,
    "INDFMPIR": 2.5,
    "CYCLE": "G",
    "SMOKING_STATUS": "Never"
}

probability = predict_respiratory_probability(
    sample_participant
)

print("--------------------------------")
print("PULMOLENS PREDICTION TEST")
print("--------------------------------")

print(
    f"Model output probability: "
    f"{probability:.4f}"
)

print(
    f"Percentage: {probability * 100:.2f}%"
)

print("--------------------------------")
print("Prediction generated successfully!")
