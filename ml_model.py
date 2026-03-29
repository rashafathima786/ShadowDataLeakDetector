import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
import random

# ✅ Generate 150 synthetic realistic data points
data = []

for _ in range(150):
    password_length = random.randint(6, 24)
    special_chars = random.randint(0, 5)
    reuse_count = random.randint(0, 5)
    login_attempts = random.randint(0, 10)

    # 🎯 Risk logic (realistic rules)
    risk_score = 0

    if password_length < 10:
        risk_score += 2
    if special_chars < 2:
        risk_score += 2
    if reuse_count > 2:
        risk_score += 2
    if login_attempts > 5:
        risk_score += 2

    leak = 1 if risk_score >= 4 else 0  # High Risk if score high

    data.append([password_length, special_chars, reuse_count, login_attempts, leak])

# ✅ Create DataFrame
df = pd.DataFrame(data, columns=[
    "password_length", "special_chars", "reuse_count", "login_attempts", "leak"
])

X = df.drop("leak", axis=1)
y = df["leak"]

# ✅ Pipeline (Scaler + RandomForest)
model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])

model.fit(X, y)

# ✅ Save model
joblib.dump(model, "model.pkl")

print("🔥 Advanced model trained with 150 data points!")