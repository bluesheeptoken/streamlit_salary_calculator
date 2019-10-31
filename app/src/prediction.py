import os
import streamlit as st
from model.serializer import Serializer


@st.cache(allow_output_mutation=True)
def cache_read_model(version):
    serializer = Serializer(os.path.join(os.getcwd(), "trained_models"))
    return serializer.read_model(version)

def write():
    with open(os.path.join(os.getcwd(), "app", "model_used.txt"), "r") as file:
        version = file.read().strip("\n")

    model, features = cache_read_model(version)

    row = []

    for numerical_feature in features[Serializer.NUMERICAL_FEATURES]:
        row.append(int(st.number_input(numerical_feature)))

    for categorical_feature, categories in features[Serializer.CATEGORICAL_FEATURES].items():
        choice = st.selectbox(categorical_feature, categories)
        for category in categories:
            row.append(int(choice == category))

    st.write(f"You salary estimation is: {model.predict([row])[0]}$ a year")
