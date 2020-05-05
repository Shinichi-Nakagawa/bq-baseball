from dataset import Table

# BigQuery Dataset
DATASET = 'mlb'

# BigQuery tables
SCHEMA_PATH = 'schema/origin'

table_parkfactor = Table(table_name='parkfactor', schema_file=f"{SCHEMA_PATH}/parkfactor.json", data_source=None)
