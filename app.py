from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Lâm Quang Khánh"

if __name__ == "__main__":
    app.run()