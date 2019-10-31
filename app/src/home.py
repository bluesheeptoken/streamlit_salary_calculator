import streamlit as st
import os


def write():
    with open(os.path.join(os.getcwd(), "app", "texts", "project_goal.md"), "r") as file:
        home_description = '\n'.join(map(lambda x: x.strip('\n'), file.readlines()))
    st.markdown(home_description)
