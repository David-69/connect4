# Development Notes for Connect 4

---
### How to check if there is a winner.

For a list of all `{colour}` tokens in the grid `map(find_winner, tokens)`.

^ Should give a list of tokens that are valid winners. If `winners != None` then declare a winner. Show winning row with Status, stop the game, display: `"{colour} is the winner!"` or something.

The list of all tokens can be `.filter`ed each turn into each `{colour}`. Then only the turn's colour list needs to be checked for a winner at the end of each turn.

---