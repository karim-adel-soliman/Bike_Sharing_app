import streamlit as st

from utils.figures import (
    plot_daily_rental_trend,
    plot_hourly_demand_by_day_type,
    plot_monthly_demand_by_year,
    plot_rental_distribution,
    plot_rider_demand_by_hour,
    plot_seasonal_demand_by_year,
    plot_seasonal_rental_distribution,
    plot_weather_demand,
)


data = st.session_state["data"]
full_data = st.session_state["df"]
show_data = st.session_state["show_data"]

st.title("Bike Sharing Demand Explorer")
st.write(
    "Explore hourly bike rentals across time, seasons, weather, and rider types."
)

# Use three columns to center the local image in the middle column
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("utils/Bicycle-sharing_systems.jpeg", width=500)

if show_data:
    st.subheader("Raw data preview")
    st.dataframe(full_data.head(10), use_container_width=True)

if data.empty:
    st.info("No records match the selected filters.")
    st.stop()

metric_total, metric_average, metric_peak = st.columns(3)
metric_total.metric("Total rentals", f"{data['cnt'].sum():,}")
metric_average.metric("Average rentals per hour", f"{data['cnt'].mean():.1f}")
peak_hour = int(data.groupby("hr")["cnt"].mean().idxmax())
metric_peak.metric("Busiest average hour", f"{peak_hour:02d}:00")

st.plotly_chart(
    plot_hourly_demand_by_day_type(data),
    use_container_width=True,
)
st.caption(
    "Non-working days include weekends and holidays. Points show average "
    "rentals for each hour, not a continuous sequence of individual trips."
)

distribution_tab, season_tab, calendar_tab, weather_tab, rider_tab = st.tabs(
    ["Distribution", "Season", "Calendar", "Weather", "Rider type"]
)

with distribution_tab:
    st.plotly_chart(plot_rental_distribution(data), use_container_width=True)

with season_tab:
    st.plotly_chart(
        plot_seasonal_rental_distribution(data),
        use_container_width=True,
    )
    st.plotly_chart(
        plot_seasonal_demand_by_year(data),
        use_container_width=True,
    )

with calendar_tab:
    st.plotly_chart(
        plot_monthly_demand_by_year(data),
        use_container_width=True,
    )
    st.plotly_chart(plot_daily_rental_trend(data), use_container_width=True)

with weather_tab:
    st.plotly_chart(plot_weather_demand(data), use_container_width=True)
    st.caption(
        "Use the chart hover data to check observation counts; severe weather "
        "categories may contain very few hours."
    )

with rider_tab:
    st.plotly_chart(
        plot_rider_demand_by_hour(data),
        use_container_width=True,
    )
