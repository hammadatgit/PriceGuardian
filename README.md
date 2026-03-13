---

# PriceGuardian — Intelligent Product Pricing Audit System

**PriceGuardian** is a **CLI-based analytics engine** that automatically audits product datasets to discover **pricing anomalies, discount irregularities, feature relationships, and data quality issues**.

The system simulates a **real-world e-commerce analytics workflow**, where messy product data must be analyzed before making pricing or marketing decisions.

PriceGuardian performs:

* Dataset health auditing
* Automatic preprocessing pipelines
* Smart column detection
* Feature engineering
* Exploratory Data Analysis (EDA)
* Pricing anomaly detection
* Feature profiling
* Automated insight generation
* Full pricing audit reports

---

# Project Goals

This project demonstrates an **end-to-end data analytics and preprocessing pipeline** including:

* Dataset auditing
* Smart schema detection
* Data preprocessing pipelines
* Feature engineering
* Exploratory Data Analysis
* Anomaly detection
* Automated reporting
* CLI-based analytics workflow
* Modular ML-ready architecture

The project also simulates **real e-commerce pricing analytics**, helping detect suspicious product prices and discount patterns.

---

# Workflow Pipeline

The system follows a structured **analytics pipeline**:

```
Raw Product Dataset
        │
        ▼
Dataset Loader
        │
        ▼
Smart Column Detection
        │
        ▼
Dataset Health Audit
        │
        ▼
Automatic Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Anomaly Detection
        │
        ▼
Feature Profiling
        │
        ▼
Insight Generation
        │
        ▼
Pricing Audit Report
```

---

# Project Structure

```
priceguardian

data/
    sample_products.csv

modules/
    loader.py
    dataset_health.py
    data_cleaner.py
    feature_builder.py
    anomaly_detector.py
    feature_profiler.py
    pricing_patterns.py
    report_generator.py
    schema_detector.py

pipelines/
    preprocessing_pipeline.py

visualization/
    plots.py

cli/
    dashboard.py

results/
    sample_products/
        plots/
        dataset_health.json
        anomaly_report.json
        feature_profile.json
        pricing_insights.json
        pricing_audit_report.json

main.py
requirements.txt
README.md
```

---

# Key Features

✔ Smart dataset loading
✔ Automatic dataset health analysis
✔ ML preprocessing pipeline using Scikit-Learn
✔ Automatic feature engineering
✔ Exploratory Data Analysis visualizations
✔ Pricing anomaly detection (Z-Score & IQR)
✔ Feature statistical profiling
✔ Business insight generation
✔ Full audit report generation
✔ CLI-based analytics workflow

---

# Smart Column Detection (Auto Dataset Understanding)

Real datasets often use **different column names**.

Example variations:

```
price
product_price
sale_price
item_price
```

PriceGuardian includes a **Schema Detection Engine** that automatically detects dataset roles.

Example detected schema:

```
Detected Columns

Price column: product_price
Discount column: sale_discount
Rating column: customer_rating
Review count column: reviews_count
Category column: product_category
```

This allows PriceGuardian to work with **any product dataset without manual configuration**.

---

# Python Concepts Covered

This project demonstrates practical implementation of:

* Pandas data analysis
* Scikit-Learn preprocessing pipelines
* Feature engineering
* Exploratory Data Analysis
* Data visualization (Matplotlib, Seaborn)
* Z-Score and IQR anomaly detection
* JSON report generation
* CLI tool development
* Modular Python architecture
* Real-world data preprocessing workflows

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/priceguardian
```

Navigate to the project folder

```
cd priceguardian
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Tool

Run the CLI dashboard:

```
python main.py
```

Example CLI session:

```
PriceGuardian – Product Pricing Audit Tool

Available datasets:

1. sample_products.csv

Select dataset number: 1
```

---

# CLI Menu Options

| Command                    | Function                     |
| -------------------------- | ---------------------------- |
| Check Dataset Health       | Analyze dataset quality      |
| Clean Dataset              | Apply preprocessing pipeline |
| Discover Pricing Patterns  | Generate engineered features |
| Find Suspicious Products   | Detect price anomalies       |
| View Product Insights      | Generate EDA visualizations  |
| Generate Full Audit Report | Export full analytics report |

---

# Generated Outputs

PriceGuardian automatically generates analytics reports.

Reports

```
results/sample_products/
```

Tables

```
dataset_health.json
feature_profile.json
anomaly_report.json
pricing_insights.json
pricing_audit_report.json
```

Plots

```
results/sample_products/plots/
```

Example plots:

* Price distribution
* Rating distribution
* Correlation heatmap

---

# Example Insights

Example insights generated by the system:

```
Average product price in dataset: 145.20

Products with discount > 40% have average rating 3.8

Price anomalies detected in 3 products
```

---

# Dataset Description

The included sample dataset simulates **an e-commerce product catalog**.

Intentional issues included:

* missing values
* extreme price values
* inconsistent brands
* discount irregularities

This simulates **real-world messy datasets used by data analysts and ML engineers.**

---

# Data Pipeline Architecture

```
                Raw Dataset
                      │
                      ▼
                Dataset Loader
                      │
                      ▼
             Schema Detection Engine
                      │
                      ▼
              Dataset Health Analyzer
                      │
                      ▼
            Automatic Cleaning Pipeline
                      │
                      ▼
               Feature Engineering
                      │
                      ▼
                EDA Visualization
                      │
                      ▼
              Anomaly Detection
                      │
                      ▼
               Insight Generator
                      │
                      ▼
               Audit Report Export
```

---

# Future Improvements

Possible extensions:

* Interactive dashboard (Streamlit)
* Natural language insight generation
* Automatic dataset schema learning
* ML-based price prediction
* PDF audit reports
* Batch analysis of multiple datasets

---

# Author

**PriceGuardian — ML Roadmap Portfolio Project**

Built as part of a **hands-on machine learning engineering learning roadmap** focusing on **data preprocessing, feature engineering, EDA, and anomaly detection.**

---
