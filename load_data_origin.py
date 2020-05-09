import pathlib
import logging

import click

from pythonjsonlogger import jsonlogger

from gcp.bq import Bq
from dataset.origin import DATASET, table_parkfactor, table_run_expectancy, table_run_value


class LoadDatabase:

    def __init__(self, filename, directory):
        self.filename = filename
        self.directory = directory
        self.bq = Bq(dataset=DATASET)
        logger = logging.getLogger()
        logHandler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter()
        logHandler.setFormatter(formatter)
        logger.addHandler(logHandler)
        self.logger = logger

    def load(self):
        if self.filename:
            self.bq.load_csv(table_id=table_parkfactor.table_name, filename=self.filename)
        if self.directory:
            p = pathlib.Path(self.directory)
            for run_ex_file in p.glob('run_ex_*.csv'):
                self.bq.load_csv(table_id=table_run_expectancy.table_name, filename=str(run_ex_file))
            for run_value_file in p.glob('run_value_*.csv'):
                self.bq.load_csv(table_id=table_run_value.table_name, filename=str(run_value_file))


@click.command()
@click.option('--filename', '-f', help='filename', type=str)
@click.option('--directory', '-d', help='file directory', type=str)
def load(filename, directory):
    cl = LoadDatabase(filename, directory)
    cl.load()


if __name__ == '__main__':
    load()
