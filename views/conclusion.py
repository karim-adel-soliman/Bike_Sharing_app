import streamlit as st


st.title("Conclusions")
st.write(
    "This analysis explores hourly bike rentals in Washington, D.C., from "
    "2011 to 2012. Use the Overview page to interact with the data and inspect "
    "how demand changes across the selected filters."
)

st.subheader("Key findings")
st.markdown(
    """
- **Time of day matters:** on working days, rentals peak during the morning and
  evening commute periods. On non-working days, demand is strongest around
  midday and early afternoon.
- **Seasonality is visible:** average hourly rentals are highest in summer and
  lowest in winter.
- **Demand is higher in 2012:** the average hourly count is higher in 2012 than
  in 2011 across each season and month in this dataset.
- **Weather and rentals are associated:** average rentals tend to be lower in
  worse weather, but the severe-weather category has very few observations, so
  its average should be interpreted cautiously.
- **Registered riders account for more rentals on average:** their hourly
  counts are higher than casual riders', and their daily patterns differ.
"""
)

st.subheader("Interpretation and limitations")
st.markdown(
    """
These findings describe patterns in the available data; they do not establish
that time, season, or weather caused changes in demand. The data covers one
city and two years, so the results may not generalize to other places or
periods. Also, `workingday = 0` combines weekends and holidays.
"""
)

st.subheader("Possible next steps")
st.markdown(
    """
- Add uncertainty intervals or sample counts to comparisons, especially for
  uncommon weather conditions.
- Compare weekday and weekend patterns separately, rather than combining
  weekends and holidays.
- If extending the project into prediction, define a clear forecasting goal
  and evaluate it with a time-based train/test split.
"""
)
