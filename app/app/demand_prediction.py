import numpy as np
from sklearn.linear_model import LinearRegression

def predict_demand(history):
    model = LinearRegression()
    X = np.array(range(len(history))).reshape(-1, 1)
    y = np.array(history)
    model.fit(X, y)
    future = np.array([[len(history)]])
    return model.predict(future)[0]
