import numpy as np
import pandas as pd


def clean_numeric(series):
    """
    Convert messy numeric columns like '10%', '20', '0.15' to float.
    """

    series = series.astype(str)

    series = series.str.replace("%", "", regex=False)

    series = pd.to_numeric(series, errors="coerce")

    return series


def build_features(df, schema):

    df = df.copy()

    price_col = schema.get("price")
    discount_col = schema.get("discount")
    rating_col = schema.get("rating")
    reviews_col = schema.get("num_reviews")
    brand_col = schema.get("brand")

    # 🔹 Clean numeric columns safely
    if price_col:
        df[price_col] = clean_numeric(df[price_col])

    if discount_col:
        df[discount_col] = clean_numeric(df[discount_col])

    if rating_col:
        df[rating_col] = clean_numeric(df[rating_col])

    if reviews_col:
        df[reviews_col] = clean_numeric(df[reviews_col])

    # 🔹 Feature Engineering
    if price_col and discount_col:

        # Convert % discount if needed
        if df[discount_col].max() > 1:
            df[discount_col] = df[discount_col] / 100

        df["final_price"] = df[price_col] * (1 - df[discount_col])

    if rating_col and reviews_col:

        df["review_score"] = df[rating_col] * np.log1p(df[reviews_col])

    if price_col and reviews_col:

        df["price_per_review"] = df[price_col] / (df[reviews_col] + 1)

    if brand_col and reviews_col:

        brand_reviews = df.groupby(brand_col)[reviews_col].mean()

        df["brand_popularity"] = df[brand_col].map(brand_reviews)

    return df