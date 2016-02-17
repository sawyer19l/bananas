Connect-4 AI
============

You will implement a Connect-4 (7 column) AI, using minimax.

Look over and understand tictactoe.py. Read the comments.

	1) Why does the method move (L98) search all of the cadidates when _minimax (L81) does the same thing?
		- Because all the candidates indicate is whether a space is free to play. Now what they individually do is much different. 
		  The method move is going to check if a given field is occupied or not and then go through all the possibilities for the next move
		  while the _minimax is going to go a step or rather a couple of steps further, it will take take the given step and return a number indicating 
	          the potential of a win given optimal future play (-2,-1,0,1,2) and to do that it will return a value, once it has iterated through field options 
		  in the move function and likewise future combinations in the _minimax function it will append them to an options list whihc will randomly select
		  between one of the favorable options for the player
		- Put simply, move calls upon the the available fields and within each field _minimax calls upon the available field that will be played
	2) What do the different return values of _minimax (L81) mean? (-2,-1,0,1,2)
		- -2 indicates a state where the other player is going to win if they play optimally, 2 is where we will win if we play optimally, 0 is a draw, and -1 and 1 
		  indicate states where we have either lost or won, respectively
	3) Why when the board count is 0 do we make the move 0?
		- it was just used for simplicity purposes since in the initial stage all the fields have the same value of 0 or tie
	4) On average how many times is _minimax (L81) called to make a move when there are N free spaces? Pick the best of (k^N for some k, N!, N, N^2)


Part 1
------

	a) Create the Board class for Connect-4. Use as much of the code from tictactoe as you can. Implment all the methods of the Board class.
	b) Create a IPlayer interface and HumanPlayer, make sure the game works.
	c) Implement minimax.

You'll notice that the program will basically not run at all. Each time minimax makes a move there are mostly another 7 moves to consider,
meaning, it grows at a rate of approximately 7^d where d are how many moves in the future searched.

After we have searched a certain depth, we need to stop searching and just try to guess how good the board is for us. (See L88)
We need a function that takes the board a real number from -1 to 1, on the favourablity of this board position. You can be as creative as you like
with this function. Try all different kinds, sometimes simple is better as you can search more moves (remember you are calling this 7^d time per move).

In competative AI tournaments, minimax solutions usually don't fair very well. Why might this be?
Hint: It's not because it's slow

BONUS: implement Alpha-Beta pruning
