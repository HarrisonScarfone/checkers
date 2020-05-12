# Checkers

This is a playable, command line checkers implementation.

## Todo

Clean repetitive code

## ...But who wants to play command line checkers?

Assuming your not into graphical style games, possibly you! 

On a more (but still not really) serious note, this is intended to be a checkers framework for machine learning.  It supports plug in
player modules, meaning you can write your own player for it.  I do intend to eventually get to it (wink wink).

## How it Works

Each game state is managed by a board object instantiated by a game manager.  The game manager and board object manage the game, prompting
each player to move on their turn by passing the player the board object and the set of all possible moves.  This should give any AI player
access to all the information about the game state that they require, and restriction selections to possible moves only.  Should a move
sequence involve jumping, only the first move will be show in the list; however the game manager will force you to select additional moves
as checkers play through jumps.
