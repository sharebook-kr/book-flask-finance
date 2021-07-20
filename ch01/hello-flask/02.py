from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p> Hello Flask </p>"


@app.route("/comp/<code>")
def comp(code):
    return f"{code} 종목입니다." 


if __name__ == "__main__":
    app.run()