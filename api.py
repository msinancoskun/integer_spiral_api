from logging import debug
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return ""



if __name__ == '__main__':
    app.run(debug=True)
    