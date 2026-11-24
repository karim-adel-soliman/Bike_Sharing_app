import streamlit as st

from utils.data import (
    DAY_TYPE_ORDER,
    SEASON_ORDER,
    WEATHER_ORDER,
    load_data,
)


st.set_page_config(
    page_title="Bike Sharing Explorer",
    page_icon="🚲",
    layout="wide",
)

df = load_data()

with st.sidebar:
    st.header("Filters")
    show_data = st.checkbox("Show raw data")
    years = sorted(df["year"].unique())
    selected_years = st.multiselect("Year", options=years, default=years)
    selected_seasons = st.multiselect(
        "Season",
        options=SEASON_ORDER,
        default=SEASON_ORDER,
    )
    selected_day_types = st.multiselect(
        "Day type",
        options=DAY_TYPE_ORDER,
        default=DAY_TYPE_ORDER,
    )
    selected_weather = st.multiselect(
        "Weather",
        options=WEATHER_ORDER,
        default=WEATHER_ORDER,
    )

filtered_data = df[
    df["year"].isin(selected_years)
    & df["season_label"].isin(selected_seasons)
    & df["day_type"].isin(selected_day_types)
    & df["weather_label"].isin(selected_weather)
].copy()

st.session_state["data"] = filtered_data
st.session_state["show_data"] = show_data
st.session_state["df"] = df

pages = [
    st.Page("views/overview.py", title="Overview", default=True),
    st.Page("views/conclusion.py", title="Conclusion"),
]
page = st.navigation(pages, position="top")
page.run()