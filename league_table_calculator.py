#!/usr/bin/python3

import sys


def league_table_results(input_file):
    league_result_stream  = open(input_file)
    league_result = league_result_stream.readlines()
    teams = []
    for index in range(len(league_result)):
        home_team_points = 0
        away_team_points = 0
        league_result[index].split(',')
        home_team = league_result[index].split(',')[0]
        home_team_name = home_team.split(' ')[:-1]
        processed_home_team_name = str.strip(' '.join(home_team_name))
        home_team_goals = int(home_team.split(' ')[-1])
        away_team = league_result[index].split(',')[1]
        away_team_name = away_team.split(' ')[:-1]
        processed_away_team_name = str.strip(' '.join(away_team_name))
        away_team_goals = int(away_team.split(' ')[-1])
        if home_team_goals > away_team_goals:
            home_team_points = 3
        elif home_team_goals == away_team_goals:
            home_team_points = 1
            away_team_points = 1
        else:
            away_team_points = 3
        team_column = [team[0] for team in teams]
        if processed_home_team_name not in team_column:
            teams.append([processed_home_team_name,int(home_team_points)])
        else:
            team_index = team_column.index(processed_home_team_name)
            teams[team_index][1] += home_team_points
        if processed_away_team_name not in team_column:
            teams.append([processed_away_team_name,int(away_team_points)])
        else:
            team_index = team_column.index(processed_away_team_name)
            teams[team_index][1] += away_team_points
    teams.sort(key = lambda x:(-x[1],x[0]))
    print(teams)

    rank =1
    for row in teams:
        points_string = 'pts'
        if int(row[1])==1:
            points_string = 'pt'
        print("{rank}. {row0}, {row1} {points_string}".format(rank=rank,row0=row[0],row1=row[1],points_string=points_string))
        rank = rank+1
    return teams

if __name__ == '__main__':
    print ('sys.argv',sys.argv)
    print('here we are')
    input_file = sys.argv[1]
    league_table_results(input_file)