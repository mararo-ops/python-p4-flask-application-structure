#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/<string:username>')
def user(Daniel):
    return f'<h1>Profile for {Daniel}</h1>'
if __name__ == '__main__':
    app.run(port=5555)