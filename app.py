from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
    
        features = [
            float(request.form["fixed acidity"]),
            float(request.form["volatile acidity"]),
            float(request.form["citric acid"]),
            float(request.form["residual sugar"]),
            float(request.form["chlorides"]),
            float(request.form["free sulfur dioxide"]),
            float(request.form["total sulfur dioxide"]),
            float(request.form["density"]),
            float(request.form["pH"]),
            float(request.form["sulphates"]),
            float(request.form["alcohol"])
        ]


        final_features = np.array(features).reshape(1, -1)


        prediction = model.predict(final_features)[0]
        prediction = round(float(prediction), 2)

        return render_template(
            "result.html",
            prediction_value=prediction
        )

    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )

