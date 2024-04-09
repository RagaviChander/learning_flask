from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world, index"


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 4444)), debug=True
    )