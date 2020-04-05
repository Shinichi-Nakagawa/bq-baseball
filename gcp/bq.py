from google.cloud import bigquery as bq
from google.cloud.bigquery import Client, LoadJobConfig

from gcp import Gcp


class Bq(Gcp):

    def __init__(self, dataset):
        super().__init__(client=Client)
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
        job_config.autodetect = True
        job_config.ignore_unknown_values = True
        job_config.source_format = source_format
        job_config.skip_leading_rows = 1
        return job_config

    def load_csv(self, table_id: str, filename: str):
        table_ref = self.dataset.table(table_id=table_id)
        with open(filename, "rb") as source_file:
            job = self.client.load_table_from_file(source_file, table_ref, job_config=self.job_config)
        return job.result()
