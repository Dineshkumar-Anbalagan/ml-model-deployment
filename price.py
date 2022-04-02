import seaborn as sns
from sklearn.linear_model import LinearRegression

def price_prediction(carat, x, y, z):
    data = sns.load_dataset("diamonds")
    data.head()

    x_data = data[["carat","x","y","z"]]
    y_data = data["price"]

    model = LinearRegression().fit(x_data, y_data)

    return model.predict([[carat, x, y, z]])