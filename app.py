from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load trained model
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        input_data = [
            float(request.form["Flength"]),
            float(request.form["Fwidth"]),
            float(request.form["Fsize"]),
            float(request.form["Fconc"]),
            float(request.form["Fconc1"]),
            float(request.form["Fasym"]),
            float(request.form["Fm3long"]),
            float(request.form["Fm3trans"]),
            float(request.form["Falpha"]),
            float(request.form["Fdist"])
        ]

        result = model.predict([input_data])

        prediction = result[0]

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)