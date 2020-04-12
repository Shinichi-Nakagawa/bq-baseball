import click
import logging

from pythonjsonlogger import jsonlogger

from gcp.bq import Bq
from dataset.lahman import DATASET, TABLES


class LoadDatabase:

    def __init__(self, directory):
        self.directory = directory
        self.bq = Bq(dataset=DATASET)
        logger = logging.getLogger()
        logHandler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        self.logger = logger

    def load(self):
        for table in TABLES:
            self.logger.info('loading table start %s', table.table_name)
            self.bq.load_csv(table_id=table.table_name, filename=f'{self.directory}/{table.data_source}')
            self.logger.info('loading table end %s', table.table_name)


@click.command()
@click.option('--directory', '-d', help='file directory', type=str, required=True)
def load(directory):
    cl = LoadDatabase(directory)
    cl.load()


if __name__ == '__main__':
    load()
