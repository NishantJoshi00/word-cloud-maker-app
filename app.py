from flask import Flask, render_template, request
from utils import get_words, remove_stopwords
from json import dumps
app = Flask(__name__)



@app.get("/")
def index():
    return render_template("index.html")


@app.post("/result")
def result():
    data = request.form.get("raw_text")
    data = remove_stopwords(get_words(data))
    return render_template("result.html", words = dumps(data))



if __name__ == "__main__":
    app.run(debug=True)
