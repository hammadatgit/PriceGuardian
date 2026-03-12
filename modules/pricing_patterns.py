import json
import os


def generate_insights(df):

    insights = []

    if "discount" in df.columns and "rating" in df.columns:

        high_discount = df[df["discount"] > 0.4]

        if len(high_discount) > 0:

            avg_rating = high_discount["rating"].mean()

            insights.append(
                f"Products with discount >40% have average rating {avg_rating:.2f}"
            )

    if "price" in df.columns:

        avg_price = df["price"].mean()

        insights.append(
            f"Average product price in dataset: {avg_price:.2f}"
        )

    return insights


def save_insights(insights, result_path):

    path = os.path.join(result_path, "pricing_insights.json")

    with open(path, "w") as f:
        json.dump(insights, f, indent=4)