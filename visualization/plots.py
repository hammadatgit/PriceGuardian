import matplotlib.pyplot as plt
import seaborn as sns
import os


def price_distribution(df, save_path, schema):

    price_col = schema.get("price")

    if not price_col:
        return

    plt.figure()

    sns.histplot(df[price_col], bins=30)

    plt.title("Price Distribution")

    file = os.path.join(save_path, "price_distribution.png")

    plt.savefig(file)

    plt.close()


def rating_distribution(df, save_path, schema):

    rating_col = schema.get("rating")

    if not rating_col:
        return

    plt.figure()

    sns.histplot(df[rating_col], bins=20)

    plt.title("Rating Distribution")

    file = os.path.join(save_path, "rating_distribution.png")

    plt.savefig(file)

    plt.close()


def correlation_heatmap(df, save_path):

    plt.figure()

    corr = df.select_dtypes(include="number").corr()

    sns.heatmap(corr, annot=True)

    file = os.path.join(save_path, "correlation_heatmap.png")

    plt.savefig(file)

    plt.close()