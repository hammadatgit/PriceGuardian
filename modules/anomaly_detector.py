import numpy as np
import pandas as pd
import json
import os


def detect_price_anomalies(df):

    price = df["price"]

    mean = price.mean()
    std = price.std()

    z_scores = (price - mean) / std

    anomalies = df[np.abs(z_scores) > 3]

    return anomalies


def detect_discount_anomalies(df):

    if "discount" not in df.columns:
        return pd.DataFrame()

    q1 = df["discount"].quantile(0.25)
    q3 = df["discount"].quantile(0.75)

    iqr = q3 - q1

    upper = q3 + 1.5 * iqr

    anomalies = df[df["discount"] > upper]

    return anomalies


def save_anomaly_report(anomalies, result_path):

    file_path = os.path.join(result_path, "anomaly_report.json")

    data = anomalies.to_dict(orient="records")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)