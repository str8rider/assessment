
# install pytest
import league_table_calculator

def test_league_table_calculator():
    correct_output= [['Tarantulas', 6],['Lions', 5],['FC Awesome',1],['Snakes', 1],['Grouches', 0]]
    test_output = league_table_calculator.league_table_results('league_result.txt') 
    assert sorted(correct_output) == sorted(test_output)