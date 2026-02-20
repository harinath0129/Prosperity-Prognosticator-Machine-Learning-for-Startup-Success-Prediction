from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("random_forest_model.pkl")

# EXACT feature order used during training
FEATURE_NAMES = [
    "age_first_funding_year",
    "age_last_funding_year",
    "age_first_milestone_year",
    "age_last_milestone_year",
    "tier_relationships",
    "funding_rounds",
    "funding_total_usd",
    "milestones",
    "avg_participants",
    "is_CA",
    "is_NY",
    "is_MA",
    "is_TX",
    "is_otherstate",
    "is_software",
    "is_web",
    "is_mobile",
    "is_enterprise",
    "has_VC",
    "has_angel",
    "has_roundA",
    "has_roundB",
    "has_roundC",
    "has_roundD",
    "is_top500",
    "dummy1", "dummy2", "dummy3", "dummy4", "dummy5",
    "dummy6", "dummy7", "dummy8", "dummy9", "dummy10", "dummy11"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("home.html")

    try:
        input_data = []

        for feature in FEATURE_NAMES:
            # take value from form if exists, else 0
            value = request.form.get(feature, 0)
            input_data.append(float(value))

        input_array = np.array(input_data).reshape(1, -1)

        prediction = model.predict(input_array)[0]
        probability = model.predict_proba(input_array)[0][1] * 100

        result = {
            "prediction": "Acquired" if prediction == 1 else "Closed",
            "success_prob": round(probability, 2),
            "failure_prob": round(100 - probability, 2)
        }

        return render_template("results.html", result=result)

    except Exception as e:
        return render_template("results.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
