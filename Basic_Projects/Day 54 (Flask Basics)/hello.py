from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def inner_function():
        text = function()
        return f"<b>{text}</b>"
    return inner_function


def make_italic(function):
    def inner_function():
        text = function()
        return f"<em>{text}</em>"
    return inner_function


def make_underlined(function):
    def inner_function():
        text = function()
        return f"<u>{text}</u>"
    return inner_function


@app.route("/")
@make_bold
@make_italic
@make_underlined
def hello_world():
    return "<p>Hello, World!!!!!!!!</p>"


@app.route("/username/<name>")
def hello_name(name):
    return f"Hello, {name}" 

if __name__ == "__main__":
    app.run(debug=True)