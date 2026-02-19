# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable Hangman game to practice core Python skills like loops, conditionals, string handling, and working with lists. By the end, you will create a complete game that responds to user input and tracks game state.

## 📝 Tasks

### 🛠️ Build the Core Hangman Loop

#### Description
Create the main game flow for Hangman. The program should choose a hidden word, display progress, and repeatedly prompt the player for guesses until the game ends.

#### Requirements
Completed program should:

- Randomly choose one word from a predefined list of at least 5 words.
- Display the hidden word as underscores (for example: `_ _ _ _ _`).
- Prompt the user to guess one letter at a time.
- Reveal all matching letter positions when the guess is correct.
- Reduce remaining attempts by 1 for each incorrect guess.


### 🛠️ Add Win/Loss Logic and Feedback

#### Description
Finish the game by handling end conditions and giving clear feedback to the player after each turn and at the end of the game.

#### Requirements
Completed program should:

- End with a win message when all letters in the word are guessed.
- End with a loss message when attempts reach 0, and show the correct word.
- Display guessed letters and remaining attempts after each turn.
- Ignore repeated guesses without reducing attempts.
- Validate input so only a single alphabetic character is accepted.

Example interaction:

```text
Word: _ _ _ _
Guess a letter: a
Correct! Word: _ a _ _
Remaining attempts: 5
```
