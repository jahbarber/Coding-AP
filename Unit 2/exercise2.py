import pandas as pd
import nfl_data_py as nfl

from helperFunctions import get_team_records, get_season_Results_By_team

schedules = get_team_records(2025)
print(schedules)



top6_Teams = ['TB','IND','LA','BUF','SF','SEA','PIT']

# Which team has the best point differential this season
# team_1=get_season_Results_By_team(2025,'TB')
team_2=get_season_Results_By_team(2025,'IND')
# team_3=get_season_Results_By_team(2025,'LA')
# team_4=get_season_Results_By_team(2025,'BUF')
# team_5=get_season_Results_By_team(2025,'SF')
# team_6=get_season_Results_By_team(2025,'SEA')

# print(team_1)
print(team_2)
# print(team_3)
# print(team_4)
# print(team_5)
# print(team_6)

#TB home:7, away:8
#IND home:64
#LA home:
#BUF home:
#SF home:
#SEA home:




# 1:IND=78

# 2:SF=-3

# 3. Which team has best home point differential this season ?
'The best home PD is INDY  64'

# 4. Which team has the best away point differential this season ?
'The best away PD is '

# def numbers():
#     total=0
# while True:
#     number_input= input("Enter the numbers (or 'done' to finish):")
#     if number_input.lower()== 'done':
#          break  
#     try:
#         number = float(number_input)  # Convert input to a float
#         total += number

#     except ValueError:
#         print("Invalid input. Please enter a number or 'done'.")

# print(f"The sum of the numbers is: {total}")







from optparse import Values


def pdCheck():
    print("please enter a number")
    number = input()
    values = []
    
    while number != 'q':
        values.append(int(number))
        print(values)
        print("please enter a number")
        number = input()
    else:
        print('doing calculation...') 
        total = sum(values)
        print(total)

    # For loop
    # Add all the numbers and return the sum of the numbers.
    # this should give us the PD.
    # HINT: you're going to be using a for loop
# for value in number:
    # print('doing calculation...')
pdCheck()