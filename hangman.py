"""

Intro
	P1 chooses word: CHOSEN_WORD

Display game
		+------+
		|	   |
		|	   
		|	  
		|     
		|
		==========
	Display '_' * number of characters in CHOSEN_WORD

Guess
	P2 guesses letter: letter_guess
    
Check
	Check in CHOSEN_WORD string for letter_guess
		If there, replace '_' with letter_guess
		Else, add body part to hangman
			+------+
			|	   |
			|	   O
			|	   |
			|     
			|
			==========
			+------+
			|	   |
			|	   O
			|	  /|
			|     
			|
			==========
			+------+
			|	   |
			|	   O
			|	  /|\
			|     
			|
			==========
			+------+
			|	   |
			|	   O
			|	  /|\
			|     /
			|
			==========
			+------+
			|	   |
			|	   O
			|	  /|\
			|     / \
			|
			==========
			+------+
			|	   |
			|	   O
			|	  
			|     
			|
			==========
    If hangman almost dead P1 has the choice to give a hint

"""

CHOSEN_WORD = input('Player 1, choose a word: ')