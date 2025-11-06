from helperFunctions import weeklyPlayerStats, plot_player_stat, plot_weekly_player_stats
import matplotlib.pyplot as plt

stats = weeklyPlayerStats(2024, "WR", 17,)  
print(stats)
# plot_player_stat(stats, stat="passing_yards", top_n=5, title="QB Passing yards (2024)", save_path="Qb_passing_yards_2024.png"  )









# 2) One-liner wrapper:
# plot_weekly_player_stats(2024, "WR", stat="rushing_tds", top_n=15, week=[1,2,3], save_path="WR_rec_rushing_td_wk1-3.png")

# Use the new plot_player_stat() and plot_weekly_player_stats() 
# to visualize the data into bar graphs and answer the following questions.


# 1. Use each helper function to find your own metric to visualize. 
# use the weeklyPlayerStats function to find positions and stat columns by name
"I created a graph showing the highest rushing touchdowns by a WR in 2021"
 
# 2. Find the player with the most touchdowns in 2024?
"Derrick Henry had the highest total touchdown at 21 TDs"


# 3. find the player with the highest total passing yards in 2024.
"Jared Goff had the highest passing yards at 4942"

# 4. which player had the highest rushing yards in week 1 and in week 17?
"Jayden Reed(week 1), and R.Pearsall"