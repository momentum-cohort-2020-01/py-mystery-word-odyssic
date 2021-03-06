import random

ANWORDS = ["h", "l", "s", "n", "m", "x", "a", "e", "i", "o"]


class Game():

    def __init__(self):  # constructor
        # self.player = Player()
        # self.open_file()
        # self.random_word(self.open_file())
        self.open_file()
        # Player()
        self.split_word = []
        self.game_word = []
        # self.playing = True
        self.letter_list = []
        self.hidden_word = []
        # self.word_list = word_list

    def open_file(self):

        with open('words.txt', 'r') as file:
            data = file.read()
        self.random_word(data)
        return data

    def select_difficulty(self, data):
        pass
        print("Welcome to the infamous word guessing game I just made up. \nIt's a non-violent version of the classic 'Hangman'. \nIf you lose, you're merely humiliated. You have 8 tries to guess the word. \nAre you ready?")

        answer = input('Please enter "y" to proceed, or press ANY key to quit')

        if answer.lower() == "y":

            print(
                'Great! \nThere are three level of difficulty: \nEasy\nMedium\nHard\nPlease choose yours')

            difficulty = input()

        else:

            print("Adios! Come back soon!")

    def random_word(self, data):

        word_list = [word for word in data.split()]
        random_word = random.choice(word_list)
        word_length = len(random_word)
        # print(f'This is the random word {random_word}')
        split_word = list(random_word)
        hidden_word = ['_' * word_length]
        guess_count = 8
        guess_letters = []

        print(
            f"I've picked a random word for you.\nIt has {word_length} characters.")

        self.validate_input(split_word, guess_count,
                            hidden_word, guess_letters, data, random_word)
        return hidden_word, split_word, guess_count, random_word, guess_letters

    def validate_input(self, split_word, guess_count, hidden_word, guess_letters, data, random_word):

        if "".join(split_word) == hidden_word:
            self.won_game(random_word, data)

        else:
            print(f'You have  {guess_count} guesses remaining.')
            print(hidden_word)
            letter = input('Please choose a letter: ')

            letter = letter.lower().strip()

            if letter in guess_letters:
                print('Sorry, you already guessed that letter!')
                self.validate_input(split_word, guess_count,
                                    hidden_word, guess_letters, data, random_word)

            if len(letter) > 1:
                print("Please only guess one letter per turn!")
                self.validate_input(split_word, guess_count,
                                    hidden_word, guess_letters, data, random_word)

            if not letter.isalpha:
                print("There are only letters in the word; please guess again.")
                self.validate_input(split_word, guess_count,
                                    hidden_word, guess_letters, data, random_word)

            if letter.isalpha and len(letter) == 1:

                if letter in split_word:
                    self.guess_right(letter, split_word, guess_count,
                                     hidden_word, guess_letters, data, random_word)
                else:
                    self.guess_wrong(letter, split_word, guess_count,
                                     hidden_word, guess_letters, data, random_word)

        return letter

    def guess_right(self, letter, split_word, guess_count, hidden_word, guess_letters, data, random_word):

        if letter in ANWORDS:
            print(f'Yes! There is an {letter} in the word!')
        else:
            print(f'Yes! There is a {letter} in the word!')

        guess_letters.append(letter)
        # print('guess letters:', guess_letters)

        hidden_word = self.alter_hidden_word(
            letter, split_word, guess_count, guess_letters, hidden_word, data, random_word)

        self.display_hidden_word(
            split_word, guess_count, guess_letters, hidden_word, data, random_word)

    def alter_hidden_word(self, letter, split_word, guess_count, guess_letters, hidden_word, data, random_word):

        if letter in guess_letters:
            return letter
        else:
            return "_"

    def display_hidden_word(self, split_word, guess_count, guess_letters, hidden_word, data, random_word):

        hidden_word = [self.alter_hidden_word(letter, split_word, guess_count, guess_letters, hidden_word, data, random_word)
                       for letter in split_word]
        hidden_word = "".join(hidden_word)
        self.validate_input(split_word, guess_count,
                            hidden_word, guess_letters, data, random_word)
        return hidden_word

    def guess_wrong(self, letter, split_word, guess_count, hidden_word, guess_letters, data, random_word):
        guess_count = guess_count - 1

        if guess_count > 0:

            if letter in ANWORDS:
                print(f'Sorry, the word does not have an {letter}!')
            else:
                print(f'Sorry, the word does not have a {letter}!')

            self.validate_input(split_word, guess_count,
                                hidden_word, guess_letters, data, random_word)

        else:
            self.lost_game(data, random_word)

        return guess_count

    def won_game(self, random_word, data):

        print(
            f'Congratulations! You won the game! \nThe word was {random_word}!\nBask in it for a few seconds.')
        print('Would you like to play again?')
        answer = input('Please enter "y" for "yes" or press ANY key to quit: ')

        if answer.lower() == "y":

            self.random_word(data)

        else:

            print("Thank you for playing. We'll see you again soon! Goodbye!")
            exit()

    def lost_game(self, data, random_word):

        print(
            f"You lost this time! \nThe hidden word was {random_word}. \nWould you like to play again? ")
        answer = input('Please enter "y" for "yes" or press ANY key to quit: ')

        if answer.lower() == "y":

            self.random_word(data)

        else:

            print("Thank you for playing. We'll see you again soon! Goodbye!")
            exit()


Game()
