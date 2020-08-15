from flask import Flask, redirect,url_for,render_template,request
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

import spacy
sp = spacy.load("en_core_web_sm")


def analyzer(sentence):
    results = sid.polarity_scores(sentence)
    print(results)
    return results

def exspacy(text):
    spacydoc = sp(text)
    doc = spacydoc.ents
    print(doc)
    return doc

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=["POST","GET"])
def getsenti():
    newresult = []
    if request.method == "POST":
        sentence = request.form["thought"]
        newresult= analyzer(sentence)
        sentiment = newresult["compound"]
        print(sentiment)
        if sentiment >=0.0:
            return redirect(url_for("results", usr="Sounds Positive!"))
        else:
            return redirect(url_for("results", usr="Just another day"))
        #return render_template("results.html", usr=sentence)
    else:
        return render_template("index.html")
       # return render_template("index.html")
@app.route("/<usr>")
def results(usr):
    return render_template("results.html", usr=usr)

@app.route("/pos.html",methods=["POST","GET"])
def tokens():
    if request.method == "POST":
        text = request.form["content"]
        doc = exspacy(text)
        return redirect(url_for("spdoc", doc=doc))

    else:
        return render_template("pos.html")


@app.route("/<doc>")
def spdoc(doc):
    return render_template("results.html", doc=doc)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
