import numpy as np


def build_features(df):

    df = df.copy()

    if "price" in df.columns and "discount" in df.columns:
        df["final_price"] = df["price"] * (1 - df["discount"])

    if "rating" in df.columns and "num_reviews" in df.columns:
        df["review_score"] = df["rating"] * np.log1p(df["num_reviews"])

    if "price" in df.columns and "num_reviews" in df.columns:
        df["price_per_review"] = df["price"] / (df["num_reviews"] + 1)

    if "brand" in df.columns and "num_reviews" in df.columns:
        brand_reviews = df.groupby("brand")["num_reviews"].mean()
        df["brand_popularity"] = df["brand"].map(brand_reviews)

    return df