# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:28:27 2024

@author: Vikrant sinha
"""

from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

app = Flask(__name__)

data = pd.read_csv("C:\\Users\\Vikrant sinha\\Downloads\\student_performance.csv")  # Replace with the correct path
X = data[["sem1_gpa", "sem2_gpa", "attendance", "assignments_completed"]]
y = data["predicted_gpa"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    sem1_gpa = data["sem1_gpa"]
    sem2_gpa = data["sem2_gpa"]
    attendance = data["attendance"]
    assignments_completed = data["assignments_completed"]

    student_df = pd.DataFrame([[sem1_gpa, sem2_gpa, attendance, assignments_completed]],
                              columns=["sem1_gpa", "sem2_gpa", "attendance", "assignments_completed"])
    predicted_gpa = model.predict(student_df)[0]
    
    risk_threshold = 7.0
    attendance_threshold = 75
    
    assignments_threshold = 6

    if (
        predicted_gpa < risk_threshold or
        attendance < attendance_threshold or
        assignments_completed < assignments_threshold
    ):
        risk_status = "At Risk"
    else:
        risk_status = "Not At Risk"

    return jsonify({
        "Predicted GPA": round(predicted_gpa, 3),
        "Risk Status": risk_status
    })

if __name__ == "__main__":
    app.run(debug=True)
