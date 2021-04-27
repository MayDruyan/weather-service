import os
from db_handler import DBHandler
from flask import Flask, request
from data_processor import DataProcessor

weather_app = Flask(__name__)
weather_app.config.from_object(os.environ['APP_SETTINGS'])
weather_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
data_processor = DataProcessor(weather_app)
db_handler = DBHandler.get_instance(weather_app)
weather_app.app_context().push()


@weather_app.route('/weather/data', methods=['GET'])
def get_data_by_location():
    data = request.get_json()
    try:
        longitude = data["lon"]
        latitude = data["lat"]
        results = db_handler.query_db_by_location(longitude, latitude)
        return results
    except Exception as e:
        return str(e), 400


@weather_app.route('/weather/summarize', methods=['GET'])
def summarize_by_location():
    data = request.get_json()
    try:
        longitude = data["lon"]
        latitude = data["lat"]
        result = db_handler.query_db_summarize_location(longitude, latitude)
        return result
    except Exception as e:
        return str(e), 400


if __name__ == '__main__':
    data_processor.process_files()
    weather_app.run(debug=True)
