# Marketing_Evaluate_simple_linear_regression
Evaluate_simple_linear_regression

# Marketing_Evaluate_simple_and_multiple_regression

An end-to-end data science project focused on evaluating simple linear regression, multiple linear regression, ANOVA tests, and hypothesis testing using Python, backed by an interactive [Streamlit](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py) web application.

---

## 🎯 End Goal & Objectives

The primary objective of this repository is to analyze marketing and sales performance data using statistical modeling and machine learning in Python to:
1. **Evaluate simple relationships**: Predict sales based on a single marketing channel using **simple linear regression**.
2. **Evaluate multiple relationships**: Predict sales using multiple marketing variables and influencer categories simultaneously using **multiple linear regression**.
3. **Run Statistical Tests**: Validate assumptions and check for group variances using **ANOVA** and **hypothesis testing**.
4. **Interact Visually**: Explore models dynamically through a local [Streamlit](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py) browser application.

---

## 📂 Repository Structure & File Breakdown

* **[`Activity_Evaluate simple linear regression.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Activity_Evaluate%20simple%20linear%20regression.ipynb)**: 
  * *What it is*: A core data science notebook focused on simple linear regression fundamentals.
  * *What it does*: Walks through loading [`marketing_and_sales_data_evaluate_lr.csv`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/marketing_and_sales_data_evaluate_lr.csv), checking linear regression assumptions (linearity, normality, homoscedasticity), fitting the model, and interpreting coefficients and $R^2$.
* **[`Marketitng_Perform multiple linear regression.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Marketitng_Perform%20multiple%20linear%20regression.ipynb)**: 
  * *What it is*: An advanced notebook expanding from single-variable to multi-variable modeling.
  * *What it does*: Utilizes [`marketing_sales_data (1).csv`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/marketing_sales_data%20(1).csv) to build a multiple linear regression model incorporating influencer categories and evaluating multicollinearity.
* **[`Explore one-way versus two-way ANOVA tests with Python.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Explore%20one-way%20versus%20two-way%20ANOVA%20tests%20with%20Python.ipynb)** & **[`Hypothesis testing with Python.ipynb`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/Hypothesis%20testing%20with%20Python.ipynb)**:
  * *What they are*: Statistical foundation notebooks.
  * *What they do*: Perform hypothesis tests and variance analyses to verify whether differences in sales across groups are statistically significant.
* **[`streamlit_app.py`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py)**: 
  * *What it is*: A Python web app entry point.
  * *What it does*: Provides an interactive user interface to visualize regression models and dataframes locally in your browser.
* **[`requirements.txt`](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/requirements.txt)**: Pins essential dependencies (`pandas`, `scikit-learn`, `statsmodels`, `streamlit`) for deterministic environments.

---

## 🛠️ Tech Stack & Key Libraries

* **Language**: Python 3.10+
* **Data Manipulation & Analysis**: `pandas`, `numpy`, `scipy`
* **Statistical Modeling & Machine Learning**: `statsmodels`, `scikit-learn`
* **Interactive Frontend**: [Streamlit](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression/blob/main/streamlit_app.py)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression.git](https://github.com/dyyland23-glitch/Marketing_Evaluate_simple_and_multiple_regression.git)
cd Marketing_Evaluate_simple_and_multiple_regression
