from dataset import Table

# BigQuery Dataset
DATASET = 'retrosheet'

# BigQuery tables
SCHEMA_PATH = 'schema/retrosheet'

table_games = Table(table_name='games', schema_file=f"{SCHEMA_PATH}/games.json", data_source=None,
                    load_type=Table.LoadType.DATA_FRAME)
table_events = Table(table_name='events', schema_file=f"{SCHEMA_PATH}/events.json", data_source=None)
