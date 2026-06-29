from flask import Flask, render_template, request

app = Flask(__name__)

decks = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        deck_name = request.form["deck_name"]
        category = request.form["category"]

        decks.append({
            "deck_name": deck_name,
            "category": category
        })

    return render_template(
        "index.html",
        decks=decks
    )

if __name__ == "__main__":
    app.run(debug=True)