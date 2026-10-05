import streamlit as st

st.title("Marketing Regression Analysis")
st.write("Welcome to the interactive marketing dashboard!")

import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import streamlit as st

# Set page config
st.set_page_config(page_title="Marketing ROI Simulator", layout="wide")

st.title("📈 Marketing Mix & Sales Regression Dashboard")
st.markdown(
    "Simulate ad spend across **TV, Social Media, and Search Engine** channels"
    " to predict total revenue."
)


# Generate / Cache synthetic marketing dataset
@st.cache_data
def load_data():
  np.random.seed(42)
  n = 250
  tv = np.random.uniform(10, 300, n)
  social = np.random.uniform(5, 150, n)
  search = np.random.uniform(5, 100, n)
  # Simulated baseline sales + coefficients + noise
  sales = 5.0 + (0.045 * tv) + (0.18 * social) + (0.12 * search) + np.random.normal(0, 1.5, n)
  return pd.DataFrame(
      {"TV": tv, "Social_Media": social, "Search_Ads": search, "Sales": sales}
  )


df = load_data()

# Fit Regression Model
X = df[["TV", "Social_Media", "Search_Ads"]]
y = df["Sales"]
model = LinearRegression().fit(X, y)

# ----------------- SIDEBAR: INTERACTIVE INPUTS -----------------
st.sidebar.header("🎯 Campaign Budget Controls")

st.sidebar.markdown("Adjust spend (in $k) to forecast expected sales:")
tv_spend = st.sidebar.slider("TV Advertising ($k)", 0, 500, 150, step=5)
social_spend = st.sidebar.slider(
    "Social Media Ads ($k)", 0, 300, 75, step=5
)
search_spend = st.sidebar.slider(
    "Search Engine Ads ($k)", 0, 200, 50, step=5
)

# Recruiter preset buttons
st.sidebar.markdown("---")
st.sidebar.subheader("Quick Presets")
col_p1, col_p2 = st.sidebar.columns(2)
if col_p1.button("Digital Heavy"):
  tv_spend, social_spend, search_spend = 30, 220, 140
if col_p2.button("Traditional Heavy"):
  tv_spend, social_spend, search_spend = 350, 40, 25

# ----------------- MAIN METRICS -----------------
total_budget = tv_spend + social_spend + search_spend
predicted_sales = model.predict([[tv_spend, social_spend, search_spend]])[0]
baseline_sales = model.intercept_

c1, c2, c3, c4 = st.columns(4)
c1.metric(label="Total Ad Spend", value=f"${total_budget:,.1f}k")
c2.metric(
    label="Forecasted Sales",
    value=f"${predicted_sales:,.2f}k",
    delta=f"{predicted_sales - baseline_sales:+.2f}k over baseline",
)
c3.metric(
    label="Est. ROAS",
    value=(
        f"{(predicted_sales / total_budget):.2f}x"
        if total_budget > 0
        else "N/A"
    ),
)
c4.metric(label="Model R² Score", value=f"{model.score(X, y):.3f}")

st.markdown("---")

# ----------------- INTERACTIVE VISUALIZATIONS -----------------
tab1, tab2 = st.tabs(["Channel Breakdown", "Historical Data & Correlation"])

with tab1:
  col_left, col_right = st.columns(2)

  with col_left:
    st.subheader("Budget Allocation")
    spend_df = pd.DataFrame({
        "Channel": ["TV", "Social Media", "Search Ads"],
        "Spend": [tv_spend, social_spend, search_spend],
    })
    fig_pie = px.pie(
        spend_df,
        values="Spend",
        names="Channel",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

  with col_right:
    st.subheader("Marginal Channel Impact (Coefficients)")
    coef_df = pd.DataFrame({
        "Channel": ["TV", "Social Media", "Search Ads"],
        "Revenue per $1 Spent": model.coef_,
    }).sort_values("Revenue per $1 Spent", ascending=False)
    fig_bar = px.bar(
        coef_df,
        x="Revenue per $1 Spent",
        y="Channel",
        orientation="h",
        color="Revenue per $1 Spent",
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
  st.subheader("Historical Spend vs. Sales")
  selected_channel = st.selectbox(
      "Select channel to visualize against Sales:",
      ["TV", "Social_Media", "Search_Ads"],
  )
  fig_scatter = px.scatter(
      df,
      x=selected_channel,
      y="Sales",
      trendline="ols",
      title=f"{selected_channel.replace('_', ' ')} Spend vs. Sales",
      labels={"Sales": "Sales ($k)", selected_channel: "Spend ($k)"},
  )
  st.plotly_chart(fig_scatter, use_container_width=True)

# ----------------- RECR
