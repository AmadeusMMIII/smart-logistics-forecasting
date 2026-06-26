# Smart Logistics Forecasting System

An advanced data analytics and time series forecasting pipeline designed to predict daily delivery volumes and warehouse stock demand. This project benchmarks modern machine learning algorithms against traditional statistical models to optimize inventory control, prevent stockouts, and streamline logistics scheduling.

---

## Project Architecture & Structure

The repository is organized following professional data science practices to maintain clear separation between raw data, modular engineering scripts, and analytical workflows:

```text
smart-logistics-forecasting/
│
├── datasets/
│   ├── delivery_data.csv          # 500-day delivery volume historical data
│   ├── delivery_clean_data.csv    # Cleaned/processed version of delivery data
│   └── stock_demand_data.csv      # 500-day warehouse demand historical data
│
├── notebooks/
│   ├── 01_data_exploration_and_decomposition.ipynb
│   ├── 02_prophet_forecast.ipynb
│   ├── 03_arima_forecast.ipynb
│   └── 04_stock_dashboard.ipynb
│
└── scripts/
    ├── __init__.py
    └── generate_synthetic_data.py # Your data generation script
```

---

## Getting Started & Installation

### 1. Clone the Repository

```
git clone https://github.com/AmadeusMMIII/smart-logistics-forecasting.git
cd smart-logistics-forecasting
```

### 2. Set Up Your Environment & Dependencies

Ensure you have Python installed, then install the necessary data science libraries:

```
pip install -r requirements.txt
```

*(If a `requirements.txt` file is not present, manually install the stack via: `pip install pandas numpy matplotlib statsmodels prophet scikit-learn ipywidgets`)*

### 3. Initialize the Core Datasets

Run the data engine script directly from your terminal to populate the `datasets/` folder with 500 records of synthetic time series data:

```
python scripts/generate_synthetic_data.py
```

---

## Analytical Workflow & Core Insights

### Phase 1: Exploration & Additive Decomposition

* **Trend Isolation:** Captured a non-linear, compounding upward growth trajectory across 500 operational days.
* **Weekly Seasonality:** Isolated a rigorous operational rhythm where daily deliveries experience sharp drops of approximately 30 units over weekends and spike by 12+ units on weekdays.

### Phase 2: Model Benchmarking Showdown

We evaluated forecasting performance over a 30-day out-of-sample window using **Mean Absolute Error (MAE)**:

| Forecasting Model | Key Characteristics | Validation Metric (MAE) | Operational Fit |
| --- | --- | --- | --- |
| **Meta Prophet** | Curve-fitting approach; preserves high-frequency seasonal waves. | **2.92 deliveries** | 🏆 **Winner** (Highly accurate) |
| **ARIMA (5,1,0)** | Traditional statistical lag autoregression; rapidly flattens over time. | **9.13 deliveries** | Baseline (Lacks long-range seasonal memory) |

### Phase 3: Operational Stock Planning Dashboard

Applying the optimized Prophet model to warehouse operations revealed critical insights for stock management:

* **Projected Metrics:** Average daily demand is forecasted at **645.20 units**, requiring a total 30-day safety stock runway of **19,356 units**.
* **Strategic Change:** Legacy safety thresholds (**540 units**) were identified as critically flawed, creating constant false alarms. The system recommends an immediate update of the threshold baseline to **625 units**.

---

## Technology Stack

* **Language:** Python
* **Environment:** Jupyter Notebook
* **Analysis & Visuals:** Pandas, NumPy, Matplotlib, Statsmodels
* **Predictive Engines:** Meta Prophet, ARIMA (`statsmodels.tsa.arima.model`)
* **Evaluation Framework:** Scikit-learn (`mean_absolute_error`)