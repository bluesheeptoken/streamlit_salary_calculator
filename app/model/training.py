import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import sys
from serializer import Serializer


data_path = os.path.join(os.getcwd(), "data", "survey_results_public.csv")

NUMERICAL_FEATURES = ['Age', 'WorkWeekHrs']
CATEGORICAL_FEATURES = ['Student']
FEATURES = NUMERICAL_FEATURES + CATEGORICAL_FEATURES
TARGET = 'ConvertedComp'
COLUMNS = FEATURES + [TARGET]


def clean_data(df, columns):
    conditions = [
        'Age.notnull()',
        'Age <= 60',
        'ConvertedComp.notnull()',
        'WorkWeekHrs.notnull()',
        'ConvertedComp <= 312000',
        'Student.notnull()',
    ]

    return df.query(" & ".join(conditions), engine='python')[columns]


def main(dir_path, version):
    cleaned_df = clean_data(pd.read_csv(data_path), COLUMNS)

    df = pd.get_dummies(cleaned_df, prefix=CATEGORICAL_FEATURES)

    scaler = StandardScaler()
    random_forest = RandomForestClassifier()
    pipe = Pipeline([
                ('scaler', StandardScaler()),
                ('random_forest', RandomForestClassifier(n_estimators=5))
            ])

    X = df.drop(TARGET, 1)
    y = df[TARGET]

    pipe.fit(X, y)

    serializer = Serializer(dir_path)

    serializer.save_model(
        pipe,
        serializer.generate_parameters(cleaned_df, CATEGORICAL_FEATURES, NUMERICAL_FEATURES),
        version
    )

if __name__ == "__main__":
    version = sys.argv[1]
    dir_path = os.path.join(os.getcwd(), "trained_models")
    main(dir_path, version)

