import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def classify_return(x):

    if x < 10:
        return "Low"

    elif x < 14:
        return "Medium"

    else:
        return "High"

def train_model():

    df = pd.read_csv("data.csv")

    df["category"] = df["returns"].apply(classify_return)

    X = df[["years"]]

    y = df["category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LogisticRegression()

    model.fit(X_train, y_train)

    return model

def predict_return(model, years):

    prediction = model.predict([[years]])

    return prediction[0]