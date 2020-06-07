from flask import Flask, render_template

app = Flask(__name__)  # Flask class already exists; instantiate "app" as Flask class instance like so

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template("index.html")
