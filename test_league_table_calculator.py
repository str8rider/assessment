
# install pytest
import league_table_calculator

def test_league_table_required_answer_against_calculated_answer():
    correct_output= [['Tarantulas', 6],['Lions', 5],['FC Awesome',1],['Snakes', 1],['Grouches', 0]]
    test_output = league_table_calculator.league_table_results('league_result.txt') 
    assert sorted(correct_output) == sorted(test_output)

def test_league_table_required_answer_against_wrong_answer():
    incorrect_output= [['Tarantulas', 6],['Lions', 5],['FC Awesome',1],['Snakes', 1],['Grouches', 0],['Grouches', 0]]
    test_output = league_table_calculator.league_table_results('league_result.txt') 
    assert sorted(incorrect_output) != sorted(test_output)

def test_against_empty_file():
    correct_output = []
    test_output = league_table_calculator.league_table_results('league_result2.txt')
    assert sorted(correct_output) == sorted(test_output)
