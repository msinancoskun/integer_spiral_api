from flask import Flask, jsonify
from app import *


app = Flask(__name__)

layout = {}

@app.route('/')
def instructions():
    return jsonify({"instructions": "Welcome! First, use create_spiral function to create a spiral using x, y coordinates. Then, if you want to see the layout that is created, use get_layout function to see them in a json format. \nLastly, provide a layoutId to filter the spirals if there more than one, and look for a value by x, y coordinates... Cheers..."})
            


@app.route('/spiral/<int:x>/<int:y>')
def create_spiral(x, y):
    """
    Request to create a spiral using x, y coordinates
    Args:
        x (int): x coordinate
        y (int): y coordinate

    Returns:
        json: returnin a message and what to do after creating a spiral and a layoutId.
    """
    global spiral
    spiral = IntegerSpiral(x, y)
    spiral.create_layout()
    layout[spiral.layoutId] = spiral.layout
    return jsonify({'message': 'spiral has been initialized. Go to /get_layout...',
                    'layoutId': spiral.layoutId})


@app.route('/get_layout')
def get_layout():
    """
    This method returns all created layouts with their ids
    Returns:
        [json]: returnin the layout in a json format.
    """
    return jsonify({'layout': layout})


@app.route('/get_value/<layoutId>/<int:x>/<int:y>/item')
def get_value(layoutId, x, y):
    """
    This method returns a data type json by checking the layout using layoutId and x, y coordinates to reach the value that they hold.
    Args:
        layoutId ([str]): Id that matches with the data.
        x (int): x coordinate
        y (int): y coordinate

    Returns:
        [json]: [returning a json message with layoutId, and x, y coordinates]
    """
    if layoutId in layout:
        print(layout[layoutId][x][y])
        return jsonify({'message': "The value held by x: '{}', y: '{}' coordinates and with layoutId: {} is '{}'".format(x, y, layoutId, layout[layoutId][x][y])})


if __name__ == '__main__':
    app.run(debug=True)
