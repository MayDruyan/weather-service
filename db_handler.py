from models import DataPoint, db
import pandas as pd

INDENTATION = 4
DB_NAME = "data_point"


class DBHandler:
    __instance = None

    @staticmethod
    def get_instance(weather_app):
        """ Static access method. """
        if DBHandler.__instance is None:
            DBHandler(weather_app)
        return DBHandler.__instance

    def __init__(self, weather_app):
        """ Virtually private constructor. """
        if DBHandler.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            DBHandler.__instance = self
            db.init_app(weather_app)

    def get_db(self):
        return db

    def check_if_row_exists_by_location(self, longitude, latitude):
        return db.session.query(db.exists().where(DataPoint.longitude == longitude and DataPoint.latitude == latitude)).scalar()

    def query_db_by_location(self, longitude, latitude):
        df = pd.read_sql(f"SELECT * "
                         f"FROM {DB_NAME} WHERE longitude={longitude} AND latitude={latitude}", db.session.bind)
        df = df.transpose()
        return df.to_json(indent=INDENTATION, date_format='iso')

    def query_db_summarize_location(self, longitude, latitude):
        df = pd.read_sql(f"SELECT "
                         f"MIN(temperature) AS min_temperature, "
                         f"MIN(precipitation) AS min_precipitation, "
                         f"MAX(temperature) AS max_temperature, "
                         f"MAX(precipitation) AS max_precipitation, "
                         f"AVG(temperature) AS avg_temperature, "
                         f"AVG(precipitation) AS avg_precipitation "
                         f"FROM {DB_NAME} WHERE longitude={longitude} AND latitude={latitude}", db.session.bind)
        df = df.transpose()
        return df.to_json(indent=INDENTATION)
