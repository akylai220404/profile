from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/photos")
@app.route("/photos/<tag>")
def photos(tag=""):
    photos = [
        "https://images.app.goo.gl/hvzJjZLZounfyrze7",
        "https://images.app.goo.gl/Mx17suoMkHeF2YeaA",
        "https://images.app.goo.gl/D45HfG1Awu4o7ZVh9"
    ]
    return render_template("photos.html", tag=tag, photos=photos)

@app.route("/hobby")
def hobby():
    return render_template("hobby.html")