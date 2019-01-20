from flask import Flask
from assets.lunch_manager import LunchManager
app = Flask(__name__)


lunch_manager = LunchManager()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/lunch')
def choose_lunch():
    print('choosing a lunch')
    return lunch_manager.choose_lunch()


@app.route('lunch/add', method='POST')
def add_location():
    # TODO: make it so people can add locations
    # have to identify what part of the request/response we need for input
    pass


if __name__ == "__main__":
    app.run()
