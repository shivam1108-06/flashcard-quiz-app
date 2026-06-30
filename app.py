from flask import Flask, render_template, request, redirect

app = Flask(__name__)

decks = []
flashcards = []
score = 0

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

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_flashcard(index):

    if request.method == "POST":

        flashcards[index]["question"] = request.form["question"]

        flashcards[index]["answer"] = request.form["answer"]

        return redirect("/")

    return render_template(
        "edit.html",
        card=flashcards[index]
    )

@app.route("/quiz/<int:index>")
def quiz(index):

    if len(flashcards) == 0:

        return "No flashcards available!"

    if index >= len(flashcards):

        index = 0

    return render_template(
        "quiz.html",
        card=flashcards[index],
        index=index,
        total=len(flashcards),
        score=score
)

@app.route("/quiz")
def start_quiz():

    return redirect("/quiz/0")

@app.route("/correct")
def correct():

    global score

    score += 1

    return redirect("/quiz/0")

if __name__ == "__main__":
    app.run(debug=True)