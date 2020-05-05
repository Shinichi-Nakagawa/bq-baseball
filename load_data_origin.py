import click
import logging

from pythonjsonlogger import jsonlogger

from gcp.bq import Bq
from dataset.origin import DATASET, table_parkfactor


class LoadDatabase:

    def __init__(self, filename):
        self.filename = filename
        self.bq = Bq(dataset=DATASET)
        logger = logging.getLogger()
        logHandler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        self.logger = logger

    def load(self):
        self.bq.load_csv(table_id=table_parkfactor.table_name, filename=self.filename)


@click.command()
@click.option('--filename', '-f', help='filename', type=str, required=True)
def load(filename):
    cl = LoadDatabase(filename)
    cl.load()


if __name__ == '__main__':
    load()
