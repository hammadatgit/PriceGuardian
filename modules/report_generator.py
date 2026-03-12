import json
import os


def generate_full_report(result_path):

    report = {}

    files = [
        "dataset_health.json",
        "feature_profile.json",
        "pricing_insights.json",
        "anomaly_report.json"
    ]

    for file in files:

        path = os.path.join(result_path, file)

        if os.path.exists(path):

            with open(path) as f:

                report[file] = json.load(f)

    final_path = os.path.join(result_path, "pricing_audit_report.json")

    with open(final_path, "w") as f:

        json.dump(report, f, indent=4)

    return final_path