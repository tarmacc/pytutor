from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.j2")

@app.route('/test')
def test():
    return render_template("test.j2")


@app.route('/elements')
def elements():
    return render_template("elements.j2")
