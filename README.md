# Great Learning - Roll a Dice

## Prerequisites
- Python 2.7.17

## Assumptions/Clarifications
- Game can be played between 2 or more players with target grater than 0
- User can get infinite chances if he gets 6 everytime
- The game continues till all the players have reach their target (Last player has to roll the dice until he reaches the target)
- The conditions on getting 6 and 1 on the dice do not work on the last player playing without opponent
- Player with higher points gets the lower rank
- Ranks of players with same points remain same as before
- After achieving the target points, rank of winners does not change


## Starting the project
- Navigate to {PROJECT_HOME}.
- Execute
  ```
    python app.py <number_of_players> <minimum_score>
  ```
  Note: Replace <number_of_players> with number of players and <minimum_score> with minimum score to be achieved by players.

## Tests
- Execute
  ```
   python -m GreatLearning.tests.playground_test
  ```
  to run the tests.