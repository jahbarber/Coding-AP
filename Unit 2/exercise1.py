import pandas as pd
import nfl_data_py as nfl

from helperFunctions import get_team_records

schedules = nfl.import_schedules([2023])

#print(schedules.columns.tolist())

records = get_team_records(2020)

print(records[['team','points_for','points_against']])


# print(records[[' wins']].mean())