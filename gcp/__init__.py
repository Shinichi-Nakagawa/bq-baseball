import os
from tempfile import NamedTemporaryFile


class Gcp:

    def __init__(self, client):
        """
        Create Client
        :param client: GCP Client class
        """
        with NamedTemporaryFile('w') as f:
            f.write(os.getenv('GCP_AUTH'))
            f.flush()
            self.client = client.from_service_account_json(f.name)
        self.client.project = os.getenv('GCP_PROJECT')

