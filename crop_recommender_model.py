import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import warnings
import os

df = pd.read_csv("Crop_recommendation.csv")

categorical_cols = ['label']

encoders = {} 


for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le 

    X = df.drop ('label', axis = 1)

    print(X)

    y = df['label']

    print(y)

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)


    joblib.dump(model, "crop_recommend_model")
    joblib.dump(encoders, "crop_recommend_encoders")

print("Files saved in:", os.getcwd())