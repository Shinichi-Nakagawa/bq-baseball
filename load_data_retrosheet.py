import pathlib
import click
import logging

import pandas as pd
from pythonjsonlogger import jsonlogger

from gcp.bq import Bq
from dataset.retrosheet import DATASET, table_games, table_events


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
        p = pathlib.Path(self.directory)
        # game data
        for csv_file in p.glob('games-*.csv'):
            df = pd.read_csv(csv_file)
            # 日付型に変換
            df['GAME_DT'] = pd.to_datetime(df['GAME_DT'], format='%Y%m%d')
            self.bq.load_dataframe(table_id=table_games.table_name, df=df)
            print('export', csv_file)
        # event data
        for csv_file in p.glob('events-*.csv'):
            self.bq.load_csv(table_id=table_events.table_name, filename=str(csv_file))
            print('export', csv_file)


@click.command()
@click.option('--directory', '-d', help='file directory', type=str, required=True)
def load(directory):
    cl = LoadDatabase(directory)
    cl.load()


if __name__ == '__main__':
    load()
