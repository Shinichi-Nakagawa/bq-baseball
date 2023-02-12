import click
import logging

import pandas as pd
from pythonjsonlogger import jsonlogger

from gcp.bq import Bq
from dataset import Table
from dataset.lahman import TABLES, RENAME_COLUMNS
from environment import DATASET_LAHMAN as DATASET


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
            if table.load_type == Table.LoadType.CSV:
                self.bq.load_csv(table_id=table.table_name, filename=f'{self.directory}/{table.data_source}')
            elif table.load_type == Table.LoadType.DATA_FRAME:
                df = pd.read_csv(f'{self.directory}/{table.data_source}')
                df.rename(columns=RENAME_COLUMNS, inplace=True)
                self.bq.load_dataframe(table_id=table.table_name, df=df)
            self.logger.info('loading table end %s', table.table_name)


@click.command()
@click.option('--directory', '-d', help='file directory', type=str, required=True)
def load(directory):
    cl = LoadDatabase(directory)
    cl.load()


if __name__ == '__main__':
    load()
