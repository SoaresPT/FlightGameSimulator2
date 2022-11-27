from flask import Flask, render_template, request
from game import *
import config

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('San Francisco') == 'San Francisco':
            config.flight_origin = config.flight_destination
            config.flight_destination = "-77.032, 38.913"
    return render_template('index.html', flight_origin=config.flight_origin, flight_destination=config.flight_destination)

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True, host='0.0.0.0', port=5000)