from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello everyone! welcome to quest family and good morning"


if __name__ == "__main__":
    app.run()

