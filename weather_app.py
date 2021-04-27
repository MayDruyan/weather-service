import os
from db_handler import DBHandler
from flask import Flask, request
from data_processor import DataProcessor
from flaskthreads import AppContextThread

weather_app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
weather_app.config.from_object(env_config)
data_processor = DataProcessor(weather_app)
db_handler = DBHandler.get_instance(weather_app)
weather_app.app_context().push()


@weather_app.route('/', methods=['GET'])
def welcome_to_service():
    return "Welcome to my weather service!"


@weather_app.route('/pre_process', methods=['GET'])
def pre_process():
    thread = AppContextThread(target=data_processor.process_files)
    thread.start()
    return "Pre-processing csv files..."


@weather_app.route('/weather/data', methods=['GET'])
def get_data_by_location():
    data = request.get_json()
    try:
        if 'lon' in data and 'lat' in data:
            longitude = data["lon"]
            latitude = data["lat"]
            # Checking there is a row matching to the given longitude and latitude
            row_exists = db_handler.check_if_row_exists_by_location(longitude, latitude)
            if not row_exists:
                return f"The given longitude: {longitude} and latitude: {latitude} does not match any location in DB.", 400
            specific_location_entries = db_handler.query_db_by_location(longitude, latitude)
            return specific_location_entries
        else:
            return f"Not enough details were sent to query DB. Please enter lat as latitude and lon as longitude", 400
    except Exception as e:
        return str(e), 400


@weather_app.route('/weather/summarize', methods=['GET'])
def summarize_by_location():
    data = request.get_json()
    try:
        if 'lon' in data and 'lat' in data:
            longitude = data["lon"]
            latitude = data["lat"]
            # Checking there is a row matching to the given longitude and latitude
            row_exists = db_handler.check_if_row_exists_by_location(longitude, latitude)
            if not row_exists:
                return f"The given longitude: {longitude}, and latitude: {latitude}, does not match any location in DB.", 400
            location_summary = db_handler.query_db_summarize_location(longitude, latitude)
            return location_summary
        else:
            return f"Not enough details were sent to query DB. Please enter lat as latitude and lon as longitude", 400
    except Exception as e:
        return str(e), 400


if __name__ == '__main__':
    weather_app.run()
