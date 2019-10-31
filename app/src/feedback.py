import streamlit as st
import os


def write():
    with open(os.path.join(os.getcwd(), "app", "texts", "feedback.md"), "r") as f:
        home_description = '\n'.join(map(lambda x: x.strip('\n'), f.readlines()))
    st.markdown(home_description)
