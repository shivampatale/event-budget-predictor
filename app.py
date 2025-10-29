from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Step 1: Read form inputs
        event_type = request.form["event_type"]           # e.g. "Wedding"
        attendees = float(request.form["attendees"])      # e.g. 150
        duration = float(request.form["duration"])        # e.g. 5
        venue = request.form["venue"]                     # e.g. "Hotel"
        decoration = request.form["decoration"]           # e.g. "Premium"
        entertainment = request.form["entertainment"]     # e.g. "DJ"
        season = request.form["season"]                   # e.g. "Peak"

        # Step 2: Create DataFrame with raw values
        input_df = pd.DataFrame([{
            "Event_Type": event_type,
            "Venue": venue,
            "Decoration": decoration,
            "Entertainment": entertainment,
            "Season": season,
            "Attendees": attendees,
            "Duration": duration
        }])

        # Step 3: Predict using the model
        prediction = model.predict(input_df)[0]

        # Step 4: Show result
        return render_template("index.html", prediction_text=f"Estimated Budget: ₹{round(prediction, 2):,.0f}")

    except Exception as e:
        # Step 5: Show error if something goes wrong
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
