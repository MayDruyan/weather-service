from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    forecast_time = db.Column(db.DateTime)
    temperature = db.Column(db.Float)
    precipitation = db.Column(db.Float)

    def __init__(self, longitude, latitude, forecast_time, temperature, precipitation):
        self.longitude = longitude
        self.latitude = latitude
        self.forecast_time = forecast_time
        self.temperature = temperature
        self.precipitation = precipitation

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def __str__(self):
        return f"Datapoint: longitude: {self.longitude}, latitude: {self.latitude}, " \
               f"forecast time: {self.forecast_time},temperature: {self.temperature}c, precipitation: {self.precipitation}mm/hr"
