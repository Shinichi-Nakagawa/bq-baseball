from dataset import Table

# BigQuery Dataset
DATASET = 'mlb'

# BigQuery tables
SCHEMA_PATH = 'schema/origin'

table_parkfactor = Table(table_name='parkfactor', schema_file=f"{SCHEMA_PATH}/parkfactor.json", data_source=None)
table_run_expectancy = Table(table_name='run_expectancy', schema_file=f"{SCHEMA_PATH}/run_expectancy.json",
                             data_source=None)
table_run_value = Table(table_name='run_value', schema_file=f"{SCHEMA_PATH}/run_value.json",
                             data_source=None)
