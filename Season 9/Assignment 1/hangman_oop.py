from random import randint


class Hangman:
    from hangman_pics import HANGMAN_PICS
    __words = [word.strip() for word in open(
        "words.txt", "r") if len(word.strip()) > 3]

    def __init__(self) -> None:
        self.missedLetters = ''
        self.correctLetters = ''
        self.__secretWord = self.getRandomWord(self.__words)
        self.gameIsDone = False

    def run_the_game(self):
        print('H A N G M A N')
        while True:
            self.displayBoard()
            # Let the player enter a letter.
            self.guess = self.getGuess(
                self.missedLetters + self.correctLetters)

            if self.guess in self.__secretWord:
                self.correctLetters = self.correctLetters + self.guess

                # Check if the player has won.
                self.__foundAllLetters = True
                for i in range(len(self.__secretWord)):
                    if self.__secretWord[i] not in self.correctLetters:
                        self.__foundAllLetters = False
                        break
                if self.__foundAllLetters:
                    print('Yes! The secret word is "' +
                          self.__secretWord + '"! You have won!')
                    self.gameIsDone = True
            else:
                self.missedLetters = self.missedLetters + self.guess

                # Check if player has guessed too many times and lost.
                if len(self.missedLetters) == len(self.HANGMAN_PICS) - 1:
                    self.displayBoard()
                    print('You have run out of guesses!\nAfter ' +
                          str(len(self.missedLetters)) +
                          ' missed guesses and ' +
                          str(len(self.correctLetters)) +
                          ' correct guesse the word was "' +
                          self.__secretWord +
                          '"')
                    self.gameIsDone = True

            # Ask the player if they want to play again
            # (but only if the game is done)
            if self.gameIsDone:
                if self.playAgain():
                    self.missedLetters = ''
                    self.correctLetters = ''
                    self.gameIsDone = False
                    self.__secretWord = self.getRandomWord(self.words)
                else:
                    break

    @classmethod
    def getRandomWord(self, wordList):
        # This function returns a random string from the passed list.
        wordIndex = randint(0, len(wordList) - 1)
        return wordList[wordIndex]

    def displayBoard(self):
        print(self.HANGMAN_PICS[len(self.missedLetters)])
        print()
        print('Missed letters:', end=' ')
        for letter in self.missedLetters:
            print(letter, end=' ')
        print()
        blanks = '_' * len(self.__secretWord)
        # Replace blanks with correct guessed letters.
        for i in range(len(self.__secretWord)):
            if self.__secretWord[i] in self.correctLetters:
                blanks = blanks[:i] + self.__secretWord[i] + blanks[i+1:]
        # Show the secret word with spaces in between each letter.
        for letter in blanks:
            print(letter, end=' ')
        print()

    def getGuess(self, alreadyGuessed):
        # Returns the letter the player entered.
        # This function makes sure the player entered a single letter
        # and not something else.
        while True:
            print('Guess a letter.')
            self.guess = input()
            self.guess = self.guess.lower()
            if len(self.guess) != 1:
                print('Please enter a single letter.')
            elif self.guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
            elif self.guess not in 'abcdefghijklmnopqrstuvwxyz':
                print('Please enter a LETTER.')
            else:
                return self.guess

    def playAgain(self):
        # This function returns True if the player wants
        # to play again otherwise, it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


if __name__ == '__main__':
    p = Hangman()
    p.run_the_game()
