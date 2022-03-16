from dataset import Table

# BigQuery Dataset
DATASET = 'lahman_baseball_database'

# BigQuery tables
SCHEMA_PATH = 'schema/lahman_baseball_database'
RENAME_COLUMNS = {
    '2B': '_2B',
    '3B': '_3B',
    'year.key': 'year_key',
    'league.key': 'league_key',
    'team.key': 'team_key',
    'park.key': 'park_key',
    'park.name': 'park_name',
    'park.alias': 'park_alias',
    'span.first': 'span_first',
    'span.last': 'span_last',
}
table_all_star_full = Table(table_name='all_star_full', schema_file=f"{SCHEMA_PATH}/all_star_full.json",
                            data_source='AllstarFull.csv')
table_appearances = Table(table_name='appearances', schema_file=f"{SCHEMA_PATH}/appearances.json",
                          data_source='Appearances.csv')
table_batting = Table(table_name='batting', schema_file=f"{SCHEMA_PATH}/batting.json", data_source='Batting.csv',
                      load_type=Table.LoadType.DATA_FRAME)
table_batting_post = Table(table_name='batting_post', schema_file=f"{SCHEMA_PATH}/batting_post.json",
                           data_source='BattingPost.csv', load_type=Table.LoadType.DATA_FRAME)
table_fielding = Table(table_name='fielding', schema_file=f"{SCHEMA_PATH}/fielding.json", data_source='Fielding.csv')
table_fielding_of = Table(table_name='fielding_of', schema_file=f"{SCHEMA_PATH}/fielding_of.json",
                          data_source='FieldingOF.csv')
table_fielding_of_split = Table(table_name='fielding_of_split', schema_file=f"{SCHEMA_PATH}/fielding_of_split.json",
                                data_source='FieldingOFsplit.csv')
table_fielding_post = Table(table_name='fielding_post', schema_file=f"{SCHEMA_PATH}/fielding_post.json",
                            data_source='FieldingPost.csv')
table_home_games = Table(table_name='home_games', schema_file=f"{SCHEMA_PATH}/home_games.json",
                         data_source='HomeGames.csv', load_type=Table.LoadType.DATA_FRAME)
table_managers = Table(table_name='managers', schema_file=f"{SCHEMA_PATH}/managers.json", data_source='Managers.csv')
table_managers_half = Table(table_name='managers_half', schema_file=f"{SCHEMA_PATH}/managers_half.json",
                            data_source='ManagersHalf.csv')
table_parks = Table(table_name='parks', schema_file=f"{SCHEMA_PATH}/parks.json", data_source='Parks.csv',
                    load_type=Table.LoadType.DATA_FRAME)
table_people = Table(table_name='people', schema_file=f"{SCHEMA_PATH}/people.json", data_source='People.csv')
table_pitching = Table(table_name='pitching', schema_file=f"{SCHEMA_PATH}/pitching.json", data_source='Pitching.csv',
                       load_type=Table.LoadType.DATA_FRAME)
table_pitching_post = Table(table_name='pitching_post', schema_file=f"{SCHEMA_PATH}/pitching_post.json",
                            data_source='PitchingPost.csv', load_type=Table.LoadType.DATA_FRAME)
table_series_post = Table(table_name='series_post', schema_file=f"{SCHEMA_PATH}/series_post.json",
                          data_source='SeriesPost.csv')
table_teams = Table(table_name='teams', schema_file=f"{SCHEMA_PATH}/teams.json", data_source='Teams.csv',
                    load_type=Table.LoadType.DATA_FRAME)
table_teams_franchises = Table(table_name='teams_franchises', schema_file=f"{SCHEMA_PATH}/teams_franchises.json",
                               data_source='TeamsFranchises.csv')
table_teams_half = Table(table_name='teams_half', schema_file=f"{SCHEMA_PATH}/teams_half.json",
                         data_source='TeamsHalf.csv')

TABLES = (
    table_all_star_full,
    table_appearances,
    table_batting,
    table_batting_post,
    table_fielding,
    table_fielding_of,
    table_fielding_of_split,
    table_fielding_post,
    table_home_games,
    table_managers,
    table_managers_half,
    table_parks,
    table_people,
    table_pitching,
    table_pitching_post,
    table_series_post,
    table_teams,
    table_teams_franchises,
    table_teams_half
)
