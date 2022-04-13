from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return "HELLO WORLD by SANDIPAN v2 using tag "

if __name__=="__main__":
    app.run()