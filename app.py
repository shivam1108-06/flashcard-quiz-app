from flask import Flask, render_template, request, redirect

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


@app.route("/delete/<int:index>")
def delete_flashcard(index):

    if index < len(flashcards):

        flashcards.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)