from flask import Flask
app = Flask(__name__)

from assets.lunch_manager import LunchManager

lunch_manager = LunchManager()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/lunch')
def choose_lunch():
    return lunch_manager.choose_lunch()


if __name__ == "__main__":
    app.run()
