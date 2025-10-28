from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Read form data
    event_type = request.form["event_type"]
    attendees = int(request.form["attendees"])
    duration = int(request.form["duration"])
    venue = request.form["venue"]
    decoration = request.form["decoration"]
    entertainment = request.form["entertainment"]
    season = request.form["season"]

    # Match input order used during training
    features = [event_type, venue, decoration, entertainment, season, attendees, duration]

    # Make prediction
    prediction = model.predict([features])[0]

    return render_template("index.html", prediction_text=f"Estimated Budget: ₹{round(prediction, 2):,.0f}")

if __name__ == "__main__":
    app.run(debug=True)

