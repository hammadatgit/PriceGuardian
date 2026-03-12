import pandas as pd
import os

DATA_FOLDER = "data"
RESULTS_FOLDER = "results"


def list_datasets():
    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")]
    return files


def load_dataset(filename):
    path = os.path.join(DATA_FOLDER, filename)
    df = pd.read_csv(path)
    return df


def create_result_folder(dataset_name):
    dataset_name = dataset_name.replace(".csv", "")
    path = os.path.join(RESULTS_FOLDER, dataset_name)

    os.makedirs(path, exist_ok=True)

    plots_path = os.path.join(path, "plots")
    os.makedirs(plots_path, exist_ok=True)

    return path