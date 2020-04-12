from enum import Enum
from dataclasses import dataclass


@dataclass
class Table:

    class LoadType(Enum):
        CSV = 'csv'
        DATA_FRAME = 'df'

    table_name: str
    schema_file: str
    data_source: str
    load_type: Enum = LoadType.CSV
