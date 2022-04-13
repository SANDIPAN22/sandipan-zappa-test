from flask import Flask

app=Flask(__name__)
hello

@app.route('/')
def index():
    return "HELLO WORLD from github action"

if __name__=="__main__":
    app.run()