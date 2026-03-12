import pandas as pd
import json
import os


def analyze_dataset(df):

    summary = {}

    summary["rows"] = df.shape[0]
    summary["columns"] = df.shape[1]

    summary["missing_values"] = df.isnull().sum().to_dict()

    summary["duplicate_rows"] = int(df.duplicated().sum())

    summary["data_types"] = df.dtypes.astype(str).to_dict()

    return summary


def save_health_report(report, result_path):

    file_path = os.path.join(result_path, "dataset_health.json")

    with open(file_path, "w") as f:
        json.dump(report, f, indent=4)