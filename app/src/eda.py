import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import math
import pandas as pd
import streamlit as st


DATA_PATH = 'data/survey_results_public.csv'

@st.cache(allow_output_mutation=True)
def load_survey_results(path):
    return pd.read_csv(path)

def write():
    survey_results = load_survey_results(DATA_PATH)

    NUMERICAL_COLUMNS = ["Age", "WorkWeekHrs", "ConvertedComp"]

    for column in NUMERICAL_COLUMNS:
        plot_histogram(survey_results[column], column)

    st.write("### Quantiles")
    st.write(survey_results.quantile(q=[0.01, 0.05, 0.1, 0.9, 0.95, 0.99]))

    CATEGORICAL_COLUMNS = ['Student', 'Country']
    for column in CATEGORICAL_COLUMNS:
        plot_bar(survey_results, column)

    # st.markdown(f"### Dev type")
    # st.write(pd.get_dummies(survey_results.apply(pd.Series).stack()).sum(level=0))

def plot_histogram(serie, column_name):
    st.markdown(f"### {column_name}")
    max_serie_value = math.ceil(serie.max())
    min_val = st.slider(f"Min value {column_name}", 0, max_serie_value, 0)
    max_val = st.slider(f"Max value {column_name}", 0, max_serie_value, max_serie_value)
    plt.hist(serie.where((min_val <= serie) & (serie <= max_val)), bins=100)
    st.pyplot()

def plot_bar(survey_results, categorical_column):
    st.markdown(f"### {categorical_column}")
    survey_results[[categorical_column, "ConvertedComp"]] \
        .groupby(categorical_column).mean() \
        .sort_values("ConvertedComp", ascending=False) \
        .head(5) \
        .plot.bar(rot=0)
    st.pyplot()
