def detect_columns(df):

    schema = {
        "price": None,
        "discount": None,
        "rating": None,
        "num_reviews": None,
        "category": None,
        "brand": None
    }

    for col in df.columns:

        name = col.lower()

        if "price" in name:
            schema["price"] = col

        elif "discount" in name or "sale" in name:
            schema["discount"] = col

        elif "rating" in name or "score" in name:
            schema["rating"] = col

        elif "review" in name or "reviews" in name:
            schema["num_reviews"] = col

        elif "category" in name or "type" in name:
            schema["category"] = col

        elif "brand" in name or "company" in name:
            schema["brand"] = col

    return schema