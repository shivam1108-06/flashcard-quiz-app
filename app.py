from flask import Flask, render_template, request

app = Flask(__name__)

decks = []
flashcards = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        if "deck_name" in request.form:

            deck_name = request.form["deck_name"]
            category = request.form["category"]

            decks.append({
                "deck_name": deck_name,
                "category": category
            })

        elif "question" in request.form:

            question = request.form["question"]
            answer = request.form["answer"]

            flashcards.append({
                "question": question,
                "answer": answer
            })

    return render_template(
        "index.html",
        decks=decks,
        flashcards=flashcards
    )

if __name__ == "__main__":
    app.run(debug=True)