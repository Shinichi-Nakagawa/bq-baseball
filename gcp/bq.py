from google.cloud import bigquery as bq
from google.cloud.bigquery import Client, LoadJobConfig
import pandas as pd

from gcp import Gcp


class Bq(Gcp):

    def __init__(self, dataset):
        self.client = Client()
        self.dataset = self.client.dataset(dataset)
        self.job_config = self._job_config()

    @staticmethod
    def _job_config(source_format=bq.SourceFormat.CSV):
        """
        BQ Job config
        :param source_format: Source Format(Default: CSV)
        :return: job config
        """
        job_config = LoadJobConfig()
        job_config.write_disposition = bq.WriteDisposition.WRITE_APPEND
        job_config.autodetect = False
        job_config.ignore_unknown_values = True
        job_config.source_format = source_format
        job_config.skip_leading_rows = 1
        return job_config

    def load_csv(self, table_id: str, filename: str):
        table_ref = self.dataset.table(table_id=table_id)
        job_config = self._job_config()
        with open(filename, "rb") as source_file:
            job = self.client.load_table_from_file(source_file, table_ref, job_config=job_config)
        return job.result()

    def load_dataframe(self, table_id: str, df: pd.DataFrame):
        table_ref = self.dataset.table(table_id=table_id)
        job_config = bq.LoadJobConfig(write_disposition=bq.WriteDisposition.WRITE_TRUNCATE)
        job_config.write_disposition = bq.WriteDisposition.WRITE_TRUNCATE
        job = self.client.load_table_from_dataframe(dataframe=df, destination=table_ref, job_config=job_config)
        return job.result()
