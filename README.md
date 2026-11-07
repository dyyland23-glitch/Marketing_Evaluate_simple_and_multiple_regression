# Marketing_Evaluate_simple_linear_regression
Evaluate_simple_linear_regression

# Marketing_Evaluate_simple_and_multiple_regression: Regression Modeling & Statistical Analysis Workflows

This repository contains hands-on data science labs, statistical hypothesis tests, and end-to-end regression modeling workflows using Python, backed by an interactive [Streamlit](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py) web application.

---

## 📂 Repository Contents

### 1. Jupyter Notebooks & Labs

* **[`Activity_Evaluate simple linear regression.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Activity_Evaluate%20simple%20linear%20regression.ipynb)**
  * **Project Overview**: Demonstrates an end-to-end simple linear regression workflow to predict sales (`sales`) based on a single marketing feature (such as `social_media` or `influencer` spending) using [`marketing_and_sales_data_evaluate_lr.csv`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/marketing_and_sales_data_evaluate_lr.csv).
  * **Key Tasks & Methods**:
    * **Exploratory Data Analysis (EDA)**: Investigates relationships between marketing spend channels and sales metrics, checking linear regression assumptions like linearity, normality, and homoscedasticity.
    * **Model Training & Evaluation**: Fits a Simple Linear Regression model, analyzes residual plots, and evaluates performance using coefficient interpretation and $R^2$ scores.

* **[`Marketitng_Perform multiple linear regression.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Marketitng_Perform%20multiple%20linear%20regression.ipynb)**
  * **Project Overview**: Constructs a multiple linear regression model using [`marketing_sales_data (1).csv`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/marketing_sales_data%20(1).csv) to predict sales using multiple marketing variables and influencer categories simultaneously.
  * **Key Tasks & Methods**:
    * **Feature Engineering & Multicollinearity**: Evaluates feature relationships using correlation matrices to avoid violating multiple linear regression assumptions.
    * **Categorical Encoding**: Prepares categorical features (such as influencer tiers) for regression modeling.
    * **Model Building & Diagnostics**: Fits multi-variable regression models, evaluates coefficients, and inspects model performance.

* **[`Explore one-way versus two-way ANOVA tests with Python.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Explore%20one-way%20versus%20two-way%20ANOVA%20tests%20with%20Python.ipynb)** & **[`Hypothesis testing with Python.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Hypothesis%20testing%20with%20Python.ipynb)**
  * **Project Overview**: Statistical foundation notebooks.
  * **Key Tasks & Methods**: 
    * Performs hypothesis tests and variance analyses (one-way and two-way ANOVA) to verify whether differences in sales across different groups are statistically significant or driven by random chance.

### 2. Application & Dependencies

* **[`streamlit_app.py`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py)**
  * **Overview**: Provides an interactive [Streamlit](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py) user interface to visualize regression models and dataframes locally in your browser.
* **[`requirements.txt`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/requirements.txt)**
  * **Overview**: Pins essential dependencies (`pandas`, `scikit-learn`, `statsmodels`, `streamlit`) for deterministic environments.

---

## 🛠️ Tech Stack & Key Libraries & Functions

* **Language**: Python 3.10+
* **Data Manipulation & Analysis**: `pandas`, `numpy`, `scipy`
  * **Key Functions**: `pd.read_csv()`, `df.dropna()`, `df.groupby()`, `np.array()`, `scipy.stats`
* **Statistical Modeling & Machine Learning**: `statsmodels`, `scikit-learn`
  * **Key Functions**: `statsmodels.api.OLS()`, `smf.ols()`, `LinearRegression()`, `train_test_split()`, `StandardScaler()`
* **Interactive Frontend**: [Streamlit](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py)
  * **Key Functions**: `st.title()`, `st.sidebar()`, `st.write()`, `st.dataframe()`, `st.altair_chart()`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression.git](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression.git)
cd Marketing_Evaluate_simple_and_multiple_regression
