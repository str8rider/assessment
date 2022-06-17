League Table Calculator

The name of the program is called 'league_table_calculator.py' and uses Python version 3.8.10. 
It takes the week's league game results to produce a ranking table of the results.
It requires a file name parameter when run on the command line. 
Running the program results in the calculated ranking table being printed to the terminal. 

For example, with the file "league_result.txt" containing the current week's games:
"""
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
""",

and the output required for this given input (1):
"""
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
4. Snakes, 1 pt
5. Grouches, 0 pts
""",

running the command 'python3 league_table_calculator.py league_result.txt'
results in the following output being printed to the terminal:
"""
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
4. Snakes, 1 pt
5. Grouches, 0 pts
""",
which is the output the program is required to have.

The program comes with a pytest unit test program called 'test_league_table_calculator.py'.
This file tests whether the specific input provided above in "league_result.txt" results in the output required in reference (1) presented above.

