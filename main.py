from flask import Flask, render_template, request
from game import *
import config

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country= request.form['data']
        print(f"country: {country}")
        if country == "New York":
            print(f"Triggered")
            config.flight_origin = config.flight_destination
            print(f"Origin: {config.flight_origin}")
            config.flight_destination = config.new_york
            print(f"Destination: {config.flight_destination}")
        if country == "San Francisco":
            print(f"Triggered")
            config.flight_origin = config.flight_destination
            print(f"Origin: {config.flight_origin}")
            config.flight_destination = "-122.414, 37.776"
            print(f"Destination: {config.flight_destination}")        
    return render_template('index.html', flight_origin=config.flight_origin, flight_destination=config.flight_destination)

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True, host='0.0.0.0', port=5000)