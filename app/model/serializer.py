import json
import os
import pickle


class Serializer:
    NUMERICAL_FEATURES = "numerical_features"
    CATEGORICAL_FEATURES = "categorical_features"

    def __init__(self, path):
        self.path = path
        self._model_filename = "model.pkl"
        self._parameters_filename = "parameters.json"

    def save_model(self, model, parameters, version):
        path_to_model = os.path.join(self.path, version)
        if not os.path.exists(path_to_model):
            os.mkdir(path_to_model)
        elif os.chdir(path_to_model):
            print(f"Model already exists in {path_to_model}, delete it before creating a new one")
            sys.exit(1)

        with open(os.path.join(path_to_model, self._model_filename), "wb") as f:
            pickle.dump(model, f)

        with open(os.path.join(path_to_model, self._parameters_filename), "w") as f:
            json.dump(parameters, f)

    def read_model(self, version):
        path_to_model = os.path.join(self.path, version)

        with open(os.path.join(path_to_model, self._model_filename), "rb") as f:
            model = pickle.load(f)

        with open(os.path.join(path_to_model, self._parameters_filename), "r") as f:
            parameters = json.load(f)

        return model, parameters

    def generate_parameters(self, dataset, categorical_columns, numerical_columns):
        return {
            self.NUMERICAL_FEATURES: numerical_columns,
            self.CATEGORICAL_FEATURES: {
                category: list(dataset[category].unique()) for category in categorical_columns
            }
        }

