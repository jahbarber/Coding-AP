from helperLogic import get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, get_player_stats_by_name, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# teamSeason = get_season_Results_By_team(2024, 'PHI') 
# print(teamSeason)


# records = get_team_records(2024.)
# print(records)

# teamSeason = get_season_Results_By_team(2024, 'PHI') 
# print(teamSeason)


# Stats = get_advanced_team_records(2024)
# print(Stats)


#2. Which WR had the most targets vs their receptions (catches) in 2024

showPlayerChart= plot_weekly_player_stats(2024,"WR", stat= "targets",top_n=15, week=[1,2,3], save_path="Wr_rec_yards_wk1-3.png")
print(showPlayerChart)
# stats = weeklyPlayerStats(2024, "WR", 18,)  
# print(stats)

