# Sample project to test Streamlit 0.48.0

This project aims to test the speed of development for ML projects compared to Jupyter-notebook. Be aware the models trained with the current feature will not give you good results, this is not the point.

I tested EDA and model exposure through a web app and this architecture:

```plaintext
app/
 - app.py
 - src/
 - model/
 - texts/
```

With:
 - ̀ src` containing the pages to write
 - ̀ model` containing the training script and `Serializer` class to write and read the features used for the ML model
 - `texts` containing markdown to display

