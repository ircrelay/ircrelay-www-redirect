import os
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return redirect('http://www.ircrelay.com')


@app.route("/<slug>")
def catch_all(slug):
    return redirect('http://www.ircrelay.com/%s' % slug)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ['PORT'])
