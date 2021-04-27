import os
import logging
import pandas as pd
from db_handler import DBHandler

logging = logging.getLogger(__name__)


class DataProcessor:

    def __init__(self, weather_app):
        self.db_handler = DBHandler.get_instance(weather_app)
        self.db = self.db_handler.get_db()
        self.resources_folder = os.path.abspath('./resources')
        self.csv_files = self._get_all_csv()

    def process_files(self):
        logging.debug("processing files")
        for file in self.csv_files:
            logging.debug(file)
            self._insert_lines_to_db(file)
            logging.debug("Done entering all csv files to DB")

    def _insert_lines_to_db(self, file):
        try:
            df = pd.read_csv(file)
            df.columns = df.columns.str.lower()
            original_cols = df.columns
            df = df.rename(columns={'temperature celsius': 'temperature', 'precipitation rate in/hr': 'precipitation', 'precipitation rate mm/hr': 'precipitation'})
            df = self._convert_to_right_measurement(df, original_cols)
            df.to_sql(name='data_point', con=self.db.session.bind, if_exists='append', index=False)
        except Exception as e:
            logging.error(str(e))
            logging.error("Unable to add item to database.")

    def _get_all_csv(self):
        all_csv = []
        for file in os.listdir(self.resources_folder):
            if file.endswith(".csv"):
                file_path = os.path.join(self.resources_folder, file)
                all_csv.append(file_path)
        return all_csv

    def _convert_to_right_measurement(self, df, original_cols):
        is_celsius = any('celsius' in col_name for col_name in original_cols.values)
        if not is_celsius:
            df['temperature'] = df['temperature'].apply(self._convert_from_f_to_c)
        is_mm = any('mm' in col_name for col_name in original_cols.values)
        if not is_mm:
            df['precipitation'] = df['precipitation'].apply(self._convert_from_in_to_mm)
        return df

    @staticmethod
    def _convert_from_f_to_c(val):
        return (val - 32) / 1.8

    @staticmethod
    def _convert_from_in_to_mm(val):
        return val * 25.4


