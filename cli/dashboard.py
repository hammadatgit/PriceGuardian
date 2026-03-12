from modules.loader import list_datasets, load_dataset, create_result_folder
from modules.dataset_health import analyze_dataset, save_health_report
from modules.data_cleaner import clean_dataset, save_clean_data


def start_dashboard():

    print("\nPriceGuardian – Product Pricing Audit Tool\n")

    datasets = list_datasets()

    print("Available datasets:\n")

    for i, file in enumerate(datasets):
        print(f"{i+1}. {file}")

    choice = int(input("\nSelect dataset number: "))

    dataset_name = datasets[choice-1]

    df = load_dataset(dataset_name)

    result_path = create_result_folder(dataset_name)

    print(f"\nDataset loaded: {dataset_name}")
    print(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")

    while True:

        print("\nSelect action:\n")

        print("1. Check Dataset Health")
        print("2. Clean Dataset Automatically")
        print("3. Exit")

        action = input("\nEnter choice: ")

        if action == "1":

            report = analyze_dataset(df)

            print("\nDataset Summary\n")

            for k, v in report.items():
                print(k, ":", v)

            save_health_report(report, result_path)

            print("\nReport saved.")

        elif action == "2":

            cleaned = clean_dataset(df)

            save_clean_data(cleaned, result_path)

            print("\nCleaned dataset saved.")

        elif action == "3":

            break