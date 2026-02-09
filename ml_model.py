import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Training dataset with 4 features
data = {
    "failed_logins": [0, 1, 3, 5, 8, 10],
    "unusual_access": [0, 0, 1, 1, 1, 1],
    "password_changes": [5, 3, 1, 0, 0, 0],
    "platforms_used": [1, 2, 3, 4, 5, 6],
    "leak": [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df.drop("leak", axis=1)
y = df["leak"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "data_leak_model.pkl")

print("✅ Model retrained with 4 features and saved")
