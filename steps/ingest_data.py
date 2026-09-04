import logging

import pandas as pd
from zenml import step

class IngestData:
    #Ingesting data from data path
    def __init__(self):
        # data_path: path to the data
        self.data_path = self.data_path

    def get_data(self):
        # Ingesting data from the data_path
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)

@step
def ingest_data(data_path: str) -> pd.DataFrame:
    
    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e