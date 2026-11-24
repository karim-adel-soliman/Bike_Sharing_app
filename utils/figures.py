import plotly.express as px


def plot_rental_distribution(data):
    fig = px.histogram(
        data,
        x="cnt",
        nbins=50,
        title="Distribution of Hourly Bike Rentals",
        labels={"cnt": "Bikes rented in an hour", "count": "Number of hours"},
    )
    fig.update_layout(bargap=0.1)
    return fig


def plot_hourly_demand_by_day_type(data):
    hourly_demand = data.groupby(["hr", "day_type"], as_index=False)["cnt"].mean()

    fig = px.line(
        hourly_demand,
        x="hr",
        y="cnt",
        color="day_type",
        markers=True,
        category_orders={"day_type": ["Working day", "Non-working day"]},
        title="Average Hourly Rentals by Day Type",
        labels={
            "hr": "Hour of day",
            "cnt": "Average rentals per hour",
            "day_type": "Day type",
        },
    )
    fig.update_xaxes(dtick=2)
    return fig


def plot_seasonal_rental_distribution(data):
    fig = px.box(
        data,
        x="season_label",
        y="cnt",
        points="outliers",
        category_orders={
            "season_label": ["Winter", "Spring", "Summer", "Fall"]
        },
        title="Hourly Rental Distribution by Season",
        labels={"season_label": "Season", "cnt": "Rentals per hour"},
    )
    return fig


def plot_seasonal_demand_by_year(data):
    seasonal = data.groupby(
        ["season_label", "year"], as_index=False
    )["cnt"].mean()
    fig = px.bar(
        seasonal,
        x="season_label",
        y="cnt",
        color="year",
        barmode="group",
        category_orders={
            "season_label": ["Winter", "Spring", "Summer", "Fall"],
            "year": ["2011", "2012"],
        },
        title="Average Hourly Rentals by Season and Year",
        labels={
            "season_label": "Season",
            "cnt": "Average rentals per hour",
            "year": "Year",
        },
    )
    return fig


def plot_monthly_demand_by_year(data):
    monthly = data.groupby(["mnth", "year"], as_index=False)["cnt"].mean()
    fig = px.line(
        monthly,
        x="mnth",
        y="cnt",
        color="year",
        markers=True,
        category_orders={"year": ["2011", "2012"]},
        title="Average Hourly Rentals by Month and Year",
        labels={
            "mnth": "Month",
            "cnt": "Average rentals per hour",
            "year": "Year",
        },
    )
    fig.update_xaxes(dtick=1)
    return fig


def plot_daily_rental_trend(data):
    daily = (
        data.groupby("dteday", as_index=False)
        .agg(daily_rentals=("cnt", "sum"), hours_recorded=("cnt", "size"))
        .sort_values("dteday")
    )
    daily["year"] = daily["dteday"].dt.year.astype(str)
    daily["rolling_7d"] = daily.groupby("year")["daily_rentals"].transform(
        lambda values: values.rolling(7, min_periods=1).mean()
    )
    fig = px.line(
        daily,
        x="dteday",
        y="rolling_7d",
        color="year",
        hover_data=["daily_rentals", "hours_recorded"],
        title="Seven-Day Average of Daily Rentals",
        labels={
            "dteday": "Date",
            "rolling_7d": "Average daily rentals (7-day window)",
            "year": "Year",
            "daily_rentals": "Daily rentals",
            "hours_recorded": "Observed hours",
        },
    )
    return fig


def plot_weather_demand(data):
    weather = data.groupby(
        ["weather_label", "day_type"], as_index=False
    ).agg(mean_rentals=("cnt", "mean"), hours=("cnt", "size"))
    fig = px.bar(
        weather,
        x="weather_label",
        y="mean_rentals",
        color="day_type",
        barmode="group",
        hover_data={"hours": True},
        category_orders={
            "weather_label": [
                "Clear",
                "Mist",
                "Light Snow/Rain",
                "Heavy Rain/Snow",
            ],
            "day_type": ["Non-working day", "Working day"],
        },
        title="Average Hourly Rentals by Weather and Day Type",
        labels={
            "weather_label": "Weather",
            "mean_rentals": "Average rentals per hour",
            "day_type": "Day type",
            "hours": "Observed hours",
        },
    )
    return fig


def plot_rider_demand_by_hour(data):
    rider_hourly = (
        data.groupby("hr", as_index=False)[["casual", "registered"]]
        .mean()
        .melt(id_vars="hr", var_name="rider_type", value_name="mean_rentals")
    )
    rider_hourly["rider_type"] = rider_hourly["rider_type"].map(
        {"casual": "Casual", "registered": "Registered"}
    )
    fig = px.line(
        rider_hourly,
        x="hr",
        y="mean_rentals",
        color="rider_type",
        markers=True,
        title="Average Hourly Rentals by Rider Type",
        labels={
            "hr": "Hour of day",
            "mean_rentals": "Average rentals per hour",
            "rider_type": "Rider type",
        },
    )
    fig.update_xaxes(dtick=2)
    return fig
