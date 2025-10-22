
from flask import Flask, render_template, request, redirect, jsonify
import json, os

app = Flask(__name__)

NEWS_FILE = "news.json"
USERNAME = "writer"
PASSWORD = "1234"

def load_news():
    if not os.path.exists(NEWS_FILE):
        with open(NEWS_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
    with open(NEWS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_news(news_list):
    with open(NEWS_FILE, "w", encoding="utf-8") as f:
        json.dump(news_list, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    news = load_news()
    return render_template("index.html", news=news)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            news = load_news()
            return render_template("admin.html", news=news)
        else:
            return "Невірний логін або пароль!"
    return render_template("admin.html", news=None)

@app.route("/add_news", methods=["POST"])
def add_news():
    title = request.form.get("title")
    text = request.form.get("text")
    if title and text:
        news = load_news()
        news.insert(0, {"title": title, "text": text})
        save_news(news)
    return redirect("/admin")

@app.route("/get_news")
def get_news():
    return jsonify(load_news())

if __name__ == "__main__":
    app.run(debug=True)
