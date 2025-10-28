from flask import Flask, request, jsonify, render_template
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
    data = request.get_json()

    # Match input order used during training
    features = [
        data["Event_Type"],
        data["Venue"],
        data["Decoration"],
        data["Entertainment"],
        data["Season"],
        data["Attendees"],
        data["Duration"]
    ]

    prediction = model.predict([features])[0]
    return jsonify({"budget": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
