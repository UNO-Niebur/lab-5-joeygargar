#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    if letter.lower() in word.lower():
        return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    if letter.lower() == word[spot].lower():
        return True
    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    result = ""
    myGuess = myGuess.lower()
    word = word.lower()

    for i in range(len(word)):
        if inSpot(myGuess[i], word, i):
            result += myGuess[i].upper()
        elif inWord(myGuess[i], word):
            result += myGuess[i] 
        else:
            result += "-"

    return result





def main ():
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    guesses_left = 6 
    while guesses_left > 0:
        user = input("What is your guess? ")

        if len(user) != len(todayWord):
            print(f"Guess must be {len(todayWord)} letters.")
            continue

        feedback = rateGuess(user, todayWord)
        print("Guess:", user)
        print("Feedback:", feedback)

        if user.lower() == todayWord.lower():
            print("You got it!")
            break
    

        guesses_left -= 1
        print("Guesses left:", guesses_left)
    if guesses_left == 0:
        print("Out of guesses! The word was:", todayWord)
    

    







if __name__ == '__main__':
  main()
