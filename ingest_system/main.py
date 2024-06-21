from ingest_system.etl import ETL
import logging

DATA_URL = "http://data.gdeltproject.org/gdeltv2/20240621223000.export.CSV.zip"


def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="myapp.log", level=logging.INFO)
    logger.info("Started ETL")
    ETL().run(DATA_URL)
    logger.info("Finished ETL")


if __name__ == "__main__":
    main()
