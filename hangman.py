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

chosen_word = input('Player 1, choose a word: ')
blank_spaces = "_ " * len(chosen_word)

print(
"""
+------+
|      |
|	   
|	  
|     
|
==========
""")
print(blank_spaces)

def guess(chosen_word):
	letter_guess = input('Player 2, guess a letter: ')
	if (letter_guess in chosen_word):
		for x in chosen_word:
			if (x == letter_guess):
				print(x, end =" ")
			else:
				print("_", end =" ")
	else:
		print(0)

guess(chosen_word)