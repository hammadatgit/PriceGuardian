import pandas as pd
import os

from pipelines.preprocessing_pipeline import build_pipeline


def clean_dataset(df):

    pipeline = build_pipeline(df)

    transformed = pipeline.fit_transform(df)

    return transformed


def save_clean_data(data, result_path):

    file_path = os.path.join(result_path, "cleaned_dataset.csv")

    df = pd.DataFrame(data)

    df.to_csv(file_path, index=False)