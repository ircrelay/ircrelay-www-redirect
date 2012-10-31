import os
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect('https://ircrelay.com')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ['PORT'])
