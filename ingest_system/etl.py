from typing import Optional
from ingest_system.utils import ETLMixin
import pandas as pd
import logging


class ETL(ETLMixin):
    def extract(self, url: str) -> pd.DataFrame:
        logging.info("[ETL.extract] Extracting data from source")
        try:
            data = self._read_csv(url)
            logging.info("Sucessfully data extracted")
            return data
        except Exception as e:
            logging.error(f"[ETL.extract] Unexpected error: {e}")
            raise e

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        logging.info("[ETL.transform] Transforming data")
        data = self._maping_columns(data)
        logging.info("[ETL.transform] Data transformed sucessfully")
        # It's pending the others transforms in the test
        return data

    def load(self, data: pd.DataFrame) -> None:
        pass

    def run(self, url: str):
        data = self.extract(url)
        data = self.transform(data)
        return data
