from pathlib import Path

import pandas as pd
import streamlit as st


DATA_PATH = Path(__file__).resolve().parents[1] / "Data" / "hour.csv"

SEASON_ORDER = ["Winter", "Spring", "Summer", "Fall"]
WEATHER_ORDER = ["Clear", "Mist", "Light Snow/Rain", "Heavy Rain/Snow"]
DAY_TYPE_ORDER = ["Working day", "Non-working day"]


@st.cache_data
def load_data() -> pd.DataFrame:
    data = pd.read_csv(DATA_PATH, parse_dates=["dteday"])
    required_columns = {
        "dteday",
        "yr",
        "season",
        "mnth",
        "hr",
        "workingday",
        "weathersit",
        "casual",
        "registered",
        "cnt",
    }
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"The hourly dataset is missing required columns: {missing}")

    data["year"] = data["yr"].map({0: "2011", 1: "2012"})
    data["season_label"] = data["season"].map(
        {1: "Winter", 2: "Spring", 3: "Summer", 4: "Fall"}
    )
    data["day_type"] = data["workingday"].map(
        {0: "Non-working day", 1: "Working day"}
    )
    data["weather_label"] = data["weathersit"].map(
        {1: "Clear", 2: "Mist", 3: "Light Snow/Rain", 4: "Heavy Rain/Snow"}
    )

    for column in ("year", "season_label", "day_type", "weather_label"):
        if data[column].isna().any():
            raise ValueError(f"The dataset contains an unrecognized code in '{column}'.")

    return data
