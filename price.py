import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def price_prediction(carat, x, y, z):
    data = sns.load_dataset("diamonds")
    data.head()

    x_data = data[["carat","x","y","z"]]
    y_data = data["price"]

    model = LinearRegression().fit(x_data, y_data)

    return model.predict([[carat, x, y, z]])