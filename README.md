# Match Based Game


## Overview
A simple match-based game implemented in Python.


## Project Structure
Main creates an instance of APP which handles all app related stuff.


## How do i edit the code?
1. To edit code simply clone the project with github or gitbash.
2. Create a branch then work from there.
3. Open the project with your freffered code editor!


## How do i add more questions?
1. go to the difficulty folder and select what difficulty to change.
2. change the variable value of question_data with the same structure of that of difficulty.py (It's a  data table)
3. You can add more ascii art in ascii_library.py
4. Make sure that values in your modified array is the same structure as the one in difficulty.py so everything looks good. Heres the structure:
### Structure
- index, ASCII_Index, HintArray, PossibleAnswerArray, CorrectAnswerIndex
### Example Usage 
- [["0", ascii_library.ascii_list[0], ["Yellow", "A fruit", "Filled with Pottatium"], ["Banana", "Apple", "Yellow Mango"], 0]]


## What is threading and do we really need it?
Threading allows the program to run another block of code in parrallel with the main thread. This means that we can take user input while also displaying the HUD aswell as handling the timer without messing with the input of the user. This is similar to Tic-Tac-Toe-X but handled more gracefully here, and yes the project would be mid if there is no threading.



