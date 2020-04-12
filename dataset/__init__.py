from dataclasses import dataclass


@dataclass
class Table:
    table_name: str
    schema_file: str
    data_source: str
