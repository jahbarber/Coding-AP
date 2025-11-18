from helperLogic import get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, get_player_stats_by_name, plot_weekly_player_stats
import matplotlib.pyplot as plt

# Columns available to research based on year and position
# columnData = get_position_columns(2024, "QB")
# print(columnData)

# '1. How much does QB pass accuracy influence team wins ? '
# teamRecord = get_team_records(2024)
# print(teamRecord)

# qbData = weeklyPlayerStats(2024, 'QB')
# print(qbData)

# 'J.Allen'
# 'J.Hurts'

# playerStat= get_player_stats_by_name(2024,'J.Hurts','QB')
# print(playerStat)

'Answer: Yes, there is a relationship. based on the average qb completion %, anything above 60 % is considered a good completion number'
"also based on team records, the top 10- top teams all have had qbs that have over 65% completion percentages."


'2. Does defensive turnovers contribute to a teams win percentage ? '
'No defensive turnovers dont contribute to a teams win percentage'
'The question is relational because it is asking if defensive turnovers relate to a teams win percentage'
'I feel as though my answer is correct because when I looked at how many turnovers teams had relative to their win.'
'Teams had a lot of turnovers yet they have less wins then teams with less turnovers.'

advanceStates = get_advanced_team_records(2024)
print(advanceStates)


'3. Who has the most passing yards of all time ? '
'This question is technically unanswerable since it is unclear and it is not concise at all.'
'We dont have enough data to figure out who has the most passing yards of all time.'



# showPlayerChart= plot_weekly_player_stats(2024,"QB", stat= "Passing_yards",top_n=15, week=[1,2,3,], save_path="wr_rec_yards_wk1-3.png")