import json
import os


def profile_features(df):

    report = {}

    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:

        report[col] = {
            "mean": float(df[col].mean()),
            "std": float(df[col].std()),
            "min": float(df[col].min()),
            "max": float(df[col].max())
        }

    return report


def save_feature_profile(profile, result_path):

    path = os.path.join(result_path, "feature_profile.json")

    with open(path, "w") as f:
        json.dump(profile, f, indent=4)