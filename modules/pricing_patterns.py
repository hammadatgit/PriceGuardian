import json
import os


def generate_insights(df, schema):

    insights = []

    price_col = schema.get("price")
    discount_col = schema.get("discount")
    rating_col = schema.get("rating")

    if discount_col and rating_col:

        high_discount = df[df[discount_col] > 0.4]

        if len(high_discount) > 0:

            avg_rating = high_discount[rating_col].mean()

            insights.append(
                f"Products with discount >40% have average rating {avg_rating:.2f}"
            )

    if price_col:

        avg_price = df[price_col].mean()

        insights.append(
            f"Average product price in dataset: {avg_price:.2f}"
        )

    return insights


def save_insights(insights, result_path):

    path = os.path.join(result_path, "pricing_insights.json")

    with open(path, "w") as f:
        json.dump(insights, f, indent=4)