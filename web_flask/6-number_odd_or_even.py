#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""
from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True


@app.route("/", strict_slashes=False)
def hello():
    """
        Displays 'Hello HBNB!'.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbtn():
    """
        Displays 'HBNB'.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def templat(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """isplay a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
