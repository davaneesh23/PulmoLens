
import pandas as pd
from utils.model_loader import load_model

FEATURES = [
    "RIDAGEYR",
    "RIAGENDR",
    "RIDRETH1",
    "DMDEDUC2",
    "DMDMARTL",
    "INDFMPIR",
    "CYCLE",
    "SMOKING_STATUS"
]

def predict_respiratory_probability(input_data):

    model = load_model()

    # Convert input into a DataFrame
    input_df = pd.DataFrame(
        [input_data],
        columns=FEATURES
    )

    # Generate calibrated probability
    probability = model.predict_proba(
        input_df
    )[0, 1]

    return float(probability)
