from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world, index"

@app.route("/ragavi")
def ragavi():
    n1 = 3
    n2 = 6
    sum= n1+n2
    return str(sum)

if __name__ == "__main__":
    app.run(debug=True)