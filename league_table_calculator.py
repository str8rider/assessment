#!/usr/bin/python3

def league_table_results(input_file):
    league_result_stream  = open(input_file)
    league_result = league_result_stream.readlines() #league_result contains 
                           # match results line by line
    teams = []#teams list is the final result table and each entry combines 
          # unique team name and associated points in nested list per team.
    for index in range(len(league_result)): # parse the match results 
        home_team_points = 0             #initialise home and away team points
        away_team_points = 0
        league_result[index].split(',')  #split the match results into home 
                                      # team section and away team section
        home_team = league_result[index].split(',')[0]
         #parse home and away teams sections further to extract team name,
         #goals scored,remove leading and trailing whitespace from team name
         #(processed_home_ for eg), and cast goals scored text into integer.
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
        team_column=[team[0] for team in teams] #team_column is an index lookup
            # table for relevant team in teams result table
        if processed_home_team_name not in team_column:
            # home team not included in teams result table yet
            teams.append([processed_home_team_name,int(home_team_points)])
        else:
            team_index = team_column.index(processed_home_team_name)
            # home team is included in results table, update ponts
            teams[team_index][1] += home_team_points
        if processed_away_team_name not in team_column:
            # away team not included in teams result table yet
            teams.append([processed_away_team_name,int(away_team_points)])
        else:
            # away team is included in results table, update ponts
            team_index = team_column.index(processed_away_team_name)
            teams[team_index][1] += away_team_points
    teams.sort(key = lambda x:(-x[1],x[0])) # sort results table first by
             # descending points and then by alphabetical order
    rank =1  # display the results, starting with the team ranked #1, 
             # the first entry element which has the most points.
    for row in teams: #print each team's rank, name and points to terminal.
        points_string = 'pts'
        if int(row[1])==1:
            points_string = 'pt'
        print("{rank}. {row0}, {row1} {points_string}".format(rank=rank,row0=row[0],row1=row[1],points_string=points_string))
        rank = rank+1
    return teams

if __name__ == '__main__': # if the file is run from the command line
    import sys
    input_file = sys.argv[1]
    league_table_results(input_file)
