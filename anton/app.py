from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user_name = "123"
    return render_template("index.j2", user_name=user_name)


@app.route('/test')
def test():
    return render_template("test.j2")
