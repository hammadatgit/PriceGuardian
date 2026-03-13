import os
import pandas as pd

from modules.feature_builder import build_features
from visualization.plots import price_distribution, rating_distribution, correlation_heatmap
from modules.anomaly_detector import detect_price_anomalies, detect_discount_anomalies, save_anomaly_report
from modules.feature_profiler import profile_features, save_feature_profile
from modules.pricing_patterns import generate_insights, save_insights
from modules.report_generator import generate_full_report
from modules.loader import list_datasets, load_dataset, create_result_folder
from modules.dataset_health import analyze_dataset, save_health_report
from modules.data_cleaner import clean_dataset, save_clean_data
from modules.schema_detector import detect_columns


def start_dashboard():

    print("\nPriceGuardian – Product Pricing Audit Tool\n")

    datasets = list_datasets()

    if len(datasets) == 0:
        print("No datasets found in /data folder.")
        return

    print("Available datasets:\n")

    for i, file in enumerate(datasets):
        print(f"{i+1}. {file}")

    try:
        choice = int(input("\nSelect dataset number: "))
        dataset_name = datasets[choice - 1]
    except:
        print("Invalid dataset selection.")
        return

    df = load_dataset(dataset_name)

    result_path = create_result_folder(dataset_name)

    print(f"\nDataset loaded: {dataset_name}")
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

    # 🔹 Detect schema automatically
    schema = detect_columns(df)

    if len(schema) == 0:
        print("\n⚠ Warning: No schema detected. Some features may not work.")

    print("\nDetected Dataset Schema:")
    for k, v in schema.items():
        print(f"{k} -> {v}")

    features_generated = False

    while True:

        print("\nSelect action:\n")

        print("1. Check Dataset Health")
        print("2. Clean Dataset Automatically")
        print("3. Discover Pricing Patterns (Feature Engineering)")
        print("4. Find Suspicious Products")
        print("5. Generate EDA Plots")
        print("6. Generate Feature Profile & Insights")
        print("7. Generate Full Audit Report")
        print("8. Exit")

        action = input("\nEnter choice: ")

        # DATASET HEALTH
        if action == "1":

            report = analyze_dataset(df)

            print("\nDataset Summary\n")

            for k, v in report.items():
                print(k, ":", v)

            save_health_report(report, result_path)

            print("\nHealth report saved.")

        # DATA CLEANING
        elif action == "2":

            cleaned = clean_dataset(df)

            save_clean_data(cleaned, result_path)

            print("\nCleaned dataset saved.")

        # FEATURE ENGINEERING
        elif action == "3":

            if features_generated:
                print("\nFeatures already generated.")
            else:
                df = build_features(df, schema)
                features_generated = True
                print("\nFeature engineering completed.")

        # ANOMALY DETECTION
        elif action == "4":

            price_anom = detect_price_anomalies(df, schema)
            discount_anom = detect_discount_anomalies(df, schema)

            anomalies = pd.concat([price_anom, discount_anom])

            save_anomaly_report(anomalies, result_path)

            print("\nAnomaly report saved.")

        # EDA VISUALIZATION
        elif action == "5":

            plot_path = os.path.join(result_path, "plots")
            os.makedirs(plot_path, exist_ok=True)

            price_distribution(df, plot_path, schema)
            rating_distribution(df, plot_path, schema)
            correlation_heatmap(df, plot_path)

            print("\nEDA plots saved.")

        # FEATURE PROFILE + INSIGHTS
        elif action == "6":

            profile = profile_features(df)
            save_feature_profile(profile, result_path)

            insights = generate_insights(df, schema)
            save_insights(insights, result_path)

            print("\nFeature profile and insights saved.")

        # FULL REPORT
        elif action == "7":

            path = generate_full_report(result_path)

            print("\nFull pricing audit report saved:")
            print(path)

        # EXIT
        elif action == "8":

            print("\nExiting PriceGuardian...\n")
            break

        else:

            print("\nInvalid choice. Try again.")