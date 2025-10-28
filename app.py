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
        # Read form inputs
        event_type = request.form["event_type"]
        attendees = int(request.form["attendees"])
        duration = int(request.form["duration"])
        venue = request.form["venue"]
        decoration = request.form["decoration"]
        entertainment = request.form["entertainment"]
        season = request.form["season"]

        # Manual encoding based on training dataset
        mapping = {
            "Event_Type": {"Wedding": 0, "Birthday": 1, "Conference": 2, "Seminar": 3, "Festival": 4, "Concert": 5, "Exhibition": 6},
            "Venue": {"Banquet Hall": 0, "Hotel": 1, "Community Hall": 2, "Auditorium": 3, "Open Ground": 4},
            "Decoration": {"Basic": 0, "Premium": 1, "Luxury": 2},
            "Entertainment": {"None": 0, "DJ": 1, "Band": 2, "Speakers": 3},
            "Season": {"Peak": 0, "Off-Season": 1}
        }

        # Create DataFrame with correct column names and encoded values
        input_df = pd.DataFrame([{
            "Event_Type": mapping["Event_Type"][event_type],
            "Venue": mapping["Venue"][venue],
            "Decoration": mapping["Decoration"][decoration],
            "Entertainment": mapping["Entertainment"][entertainment],
            "Season": mapping["Season"][season],
            "Attendees": attendees,
            "Duration": duration
        }])

        # Predict budget
        prediction = model.predict(input_df)[0]

        return render_template("index.html", prediction_text=f"Estimated Budget: ₹{round(prediction, 2):,.0f}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
