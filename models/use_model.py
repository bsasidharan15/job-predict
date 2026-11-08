# use_model.py
# Purpose: Load trained model and make predictions
# Job Acceptance Prediction System

import pickle
import pandas as pd
import numpy as np
import os

MODEL_PATH = "models/best_model.pkl"
FEATURES_PATH = "models/model_features.pkl"

# Load model

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "❌ Model not found. Train model using 05_ml_modeling.ipynb first."
        )
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model


# Load feature list (VERY IMPORTANT)

def load_features():
    if not os.path.exists(FEATURES_PATH):
        raise FileNotFoundError(
            "❌ Feature list not found. Save feature names during training."
        )
    with open(FEATURES_PATH, "rb") as f:
        features = pickle.load(f)
    return features



# Prediction function

def predict_job_acceptance(candidate_dict):
    """
    candidate_dict : dict
    Returns prediction & probabilities
    """

    model = load_model()
    features = load_features()

    # Convert input to DataFrame
    input_df = pd.DataFrame([candidate_dict])

    # Ensure all required features exist
    for col in features:
        if col not in input_df.columns:
            input_df[col] = 0  # default safe value

    # Maintain column order
    input_df = input_df[features]

    # Prediction
    pred = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]

    return {
        "prediction": "Will ACCEPT" if pred == 1 else "Will REJECT",
        "probability_accept": round(float(proba[1]), 4),
        "probability_reject": round(float(proba[0]), 4),
        "confidence": round(float(max(proba)), 4),
    }



# Example usage

if __name__ == "__main__":
    print("=" * 50)
    print("JOB ACCEPTANCE PREDICTION SYSTEM")
    print("=" * 50)

    example_candidate = {
        "technical_score": 85,
        "skills_match_percentage": 90,
        "academic_index": 75,
        "overall_assessment": 80,
        "ctc_gap_percentage": 20,
        "risk_score": 0.2
    }

    print("\nInput Candidate Data:")
    for k, v in example_candidate.items():
        print(f"  {k}: {v}")

    result = predict_job_acceptance(example_candidate)

    print("\n📊 Prediction Result")
    print("-" * 30)
    print(f"Decision              : {result['prediction']}")
    print(f"Probability (Accept)  : {result['probability_accept']:.2%}")
    print(f"Probability (Reject)  : {result['probability_reject']:.2%}")
    print(f"Confidence            : {result['confidence']:.2%}")
