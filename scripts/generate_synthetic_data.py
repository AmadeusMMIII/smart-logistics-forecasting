import numpy as np
import pandas as pd


def generate_logistics_data(days=500):
    # Create date range starting Jan 1, 2025
    date_range = pd.date_range(start="2025-01-01", periods=days, freq="D")

    # Set random seed for reproducibility
    np.random.seed(42)

    # Base timelines / features
    time_index = np.arange(days)

    # --- 1. GENERATE DELIVERY VOLUME DATA ---
    # Trend: Gradual upward slope
    trend_del = 100 + (time_index * 0.15)
    # Weekly seasonality: Higher on weekdays (Mon=0, Sun=6)
    day_of_week = date_range.dayofweek
    weekly_season_del = np.where(day_of_week < 5, 25, -15)
    # Monthly seasonality: Surge around mid-month payday (days 13-17)
    monthly_season_del = np.where(
        (date_range.day >= 13) & (date_range.day <= 17), 20, 0
    )
    # Random Noise
    noise_del = np.random.normal(0, 8, days)

    deliveries = trend_del + weekly_season_del + monthly_season_del + noise_del
    deliveries = np.maximum(
        10, deliveries.astype(int)
    )  # Ensure no negative values

    df_delivery = pd.DataFrame({"date": date_range, "deliveries": deliveries})
    df_delivery.to_csv("datasets/delivery_data.csv", index=False)
    print(f"Successfully saved 500 records to 'delivery_data.csv'")

    # --- 2. GENERATE STOCK DEMAND DATA (For Day 5) ---
    # Trend: Correlated with deliveries but on a larger scale
    trend_stock = 450 + (time_index * 0.4)
    # Weekly seasonality: Restocking peaks mid-week (Wednesday/Thursday)
    weekly_season_stock = np.where((day_of_week == 2) | (day_of_week == 3), 40, -10)
    # Random Noise
    noise_stock = np.random.normal(0, 25, days)

    stock_demand = trend_stock + weekly_season_stock + noise_stock
    stock_demand = np.maximum(50, stock_demand.astype(int))

    df_stock = pd.DataFrame({"date": date_range, "stock_demand": stock_demand})
    df_stock.to_csv("datasets/stock_demand_data.csv", index=False)
    print(f"Successfully saved 500 records to 'stock_demand_data.csv'")


if __name__ == "__main__":
    generate_logistics_data(500)