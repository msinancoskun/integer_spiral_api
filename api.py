from flask import Flask, jsonify
from app import *


app = Flask(__name__)

layout = {}

@app.route('/')
def instructions():
    return "Welcome"


@app.route('/spiral/<int:x>/<int:y>')
def create_spiral(x, y):
    global spiral
    spiral = IntegerSpiral(x, y)
    spiral.create_layout()
    layout[spiral.layoutId] = spiral.layout
    return jsonify({'message': 'spiral has been initialized. Go to /get_layout...',
                    'layoutId': spiral.layoutId})


@app.route('/get_layout')
def get_layout():
    return jsonify({'layout': layout})


@app.route('/get_value/<layoutId>/<int:x>/<int:y>/item')
def get_value(layoutId, x, y):
    if layoutId in layout:
        print(layout[layoutId][x][y])
        return jsonify({'message': "The value held by x: '{}', y: '{}' coordinates and with layoutId: {} is '{}'".format(x, y, layoutId, layout[layoutId][x][y])})


if __name__ == '__main__':
    app.run(debug=True)
