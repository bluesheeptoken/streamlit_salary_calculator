import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

import src.eda
import src.home
import src.prediction
import src.feedback


st.sidebar.title("Navigation")

PAGES = {
    "Home": src.home,
    "EDA": src.eda,
    "Prediction": src.prediction,
    "Feedback": src.feedback
}

selection = st.sidebar.radio(
    "Go to",
    list(PAGES.keys())
)

PAGES[selection].write()
