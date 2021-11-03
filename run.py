inputWord = str.upper(input("Codeinstitute"))
guessedLetter = ""
wordLength = len(inputWord)
wordList = [""] * wordLength
usedLetters = [""]

letterNumber = 0
allowedGuesses = 10
rightGuesses = 0
winGuesses = 0

print("here is some info")  # game rules
print("Are you ready")
print("the word is " + str(wordLength) + " 13 letters.")
print("you have 10 tries ")
print("good luck")


while(guessedLetter != "END") and (allowedGuesses != 0):
    print(wordList)
    guessedLetter = str.upper(input("Guess a letter: "))

    while letterNumber < wordLength:
        if guessedLetter in usedLetters:
            print("you have already guessed this letter.")
            allowedGuesses += 1
            break

        elif inputWord[letterNumber] == guessedLetter:
            wordList[letterNumber] = guessedLetter
            rightGuesses = 1
            winGuesses += 1

        letterNumber += 1

        allowedGuesses -= 1-rightGuesses
        rightGuesses = 0
        letterNumber = 0

        usedLetters.append(guessedLetter)

        if winGuesses == len(inputWord):
            print(wordList)
            print("Woho, you won " + inputWord)
            break
        elif allowedGuesses == 0:
            print("game over the right word is" + inputWord)
            break
        elif guessedLetter == "END":
            break



 def main():  # code from tutorial on newlines
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()