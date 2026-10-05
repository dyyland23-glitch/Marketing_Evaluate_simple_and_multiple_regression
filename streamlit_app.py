import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st

st.set_page_config(
    page_title="Marketing & Sales Regression Evaluation", layout="wide"
)

st.title("📈 Marketing & Sales Regression Dashboard")
st.markdown(
    "Evaluating **Simple & Multiple Linear Regression** models on ad spend and"
    " sales data."
)


# 1. Load Data
@st.cache_data
def load_data():
  df = pd.read_csv("marketing_sales_data (1).csv")
  df = df.dropna()
  return df


try:
  df = load_data()
except FileNotFoundError:
  st.error(
      "File 'marketing_sales_data (1).csv' not found. Please make sure it is"
      " committed to your GitHub repository root."
  )
  st.stop()

# 2. Identify Numeric Features & Target
# Common columns in marketing_sales_data are TV, Radio, Social Media, Influencer, Sales
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

if "Sales" in df.columns:
  target_col = "Sales"
else:
  target_col = numeric_cols[-1]

feature_candidates = [col for col in numeric_cols if col != target_col]

# ----------------- SIDEBAR -----------------
st.sidebar.header("⚙️ Model Configuration")
model_type = st.sidebar.radio(
    "Select Model Type:",
    ["Multiple Linear Regression", "Simple Linear Regression"],
)

if model_type == "Simple Linear Regression":
  selected_features = [
      st.sidebar.selectbox("Choose Independent Feature (X):", feature_candidates)
  ]
else:
  selected_features = st.sidebar.multiselect(
      "Select Features (X):",
      feature_candidates,
      default=feature_candidates[:3]
      if len(feature_candidates) >= 3
      else feature_candidates,
  )

if not selected_features:
  st.warning("Please select at least one feature from the sidebar.")
  st.stop()

# ----------------- FIT MODEL -----------------
X = df[selected_features]
y = df[target_col]

model = LinearRegression().fit(X, y)
y_pred = model.predict(X)

r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

# ----------------- METRICS ROW -----------------
col1, col2, col3 = st.columns(3)
col1.metric("Features Selected", f"{len(selected_features)}")
col2.metric("R² Score (Variance Explained)", f"{r2:.4f}")
col3.metric("Root Mean Squared Error (RMSE)", f"{rmse:.2f}")

st.markdown("---")

# ----------------- INTERACTIVE SIMULATOR & TABS -----------------
tab1, tab2, tab3 = st.tabs(
    ["Interactive Simulator", "Model Analysis & Coefficients", "Raw Data"]
)

with tab1:
  st.subheader("🎯 Real-Time Sales Predictor")
  st.write("Adjust input values to simulate predicted sales:")

  input_vals = {}
  input_cols = st.columns(min(len(selected_features), 4))
  for idx, feat in enumerate(selected_features):
    min_v = float(df[feat].min())
    max_v = float(df[feat].max())
    mean_v = float(df[feat].mean())
    with input_cols[idx % len(input_cols)]:
      input_vals[feat] = st.slider(
          f"{feat} Spend", min_v, max_v, mean_v, step=1.0
      )

  input_df = pd.DataFrame([input_vals])
  simulated_pred = model.predict(input_df)[0]

  st.metric(
      label="Forecasted Sales",
      value=f"${simulated_pred:,.2f}",
      delta=f"{simulated_pred - model.intercept_:+.2f} relative to baseline intercept",
  )

with tab2:
  col_left, col_right = st.columns(2)

  with col_left:
    st.subheader("Feature Impact (Coefficients)")
    coef_df = pd.DataFrame(
        {"Feature": selected_features, "Coefficient": model.coef_}
    ).sort_values(by="Coefficient", ascending=False)

    fig_coef = px.bar(
        coef_df,
        x="Coefficient",
        y="Feature",
        orientation="h",
        color="Coefficient",
        color_continuous_scale="Blues",
    )
    st.plotly_chart(fig_coef, use_container_width=True)

  with col_right:
    st.subheader("Actual vs. Predicted Sales")
    eval_df = pd.DataFrame({"Actual": y, "Predicted": y_pred})
    fig_scatter = px.scatter(
        eval_df,
        x="Actual",
        y="Predicted",
        labels={
            "Actual": f"Actual {target_col}",
            "Predicted": f"Predicted {target_col}",
        },
        opacity=0.7,
    )
    # Add 45-degree reference line
    min_val = min(y.min(), y_pred.min())
    max_val = max(y.max(), y_pred.max())
    fig_scatter.add_shape(
        type="line",
        line=dict(dash="dash", color="red"),
        x0=min_val,
        y0=min_val,
        x1=max_val,
        y1=max_val,
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
  st.subheader("Dataset Preview")
  st.dataframe(df.head(20), use_container_width=True)
  st.caption(f"Showing top 20 rows of {df.shape[0]} total observations.")
