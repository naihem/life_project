from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    GameOfLife(20, 20)
    return render_template("index.html")

@app.route('/live')
def live(var = GameOfLife()):
    if var.counter > 0:
        var.form_new_generation()
    var.counter += 1
    return render_template("live.html", var=var)


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5000)
