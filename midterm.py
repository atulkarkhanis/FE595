from flask import Flask, redirect,url_for,render_template,request
import nltk.sentiment.vader as nk

def analyzer(sentence):
    nkobj = nk.SentimentIntensityAnalyzer()
    results = nkobj.polarity_scores(sentence)
    print(results)
    return results

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/",methods=["POST","GET"])
def getsenti():
    if request.method == "POST":
        sentence = request.form["thought"]
        response = analyzer(sentence)
        return redirect(url_for("results",usr=sentence))
    else:
        return render_template("index.html")
@app.route("/results")
def user(usr):
    return render_template("results.html", usr=usr)

if __name__ == "__main__":
    app.run()
