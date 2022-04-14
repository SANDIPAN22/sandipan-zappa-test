from flask import Flask

app=Flask(__name__)


@app.route('/')
def index():
    return "HELLO WORLD by SANDIPAN April 14/2022 poision"

if __name__=="__main__":
    app.run()