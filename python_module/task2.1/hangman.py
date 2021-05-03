import random
import json
from datetime import datetime

class Hangman:
    def __init__(self, lives):
        self.word = self.get_random_word('words.txt')
        self.letters_tried = []
        self.guessed = False
        self.lives = lives

    def guess(self, inp):
        if len(inp) > 1:
            self._guess_word(inp)
        else:
            self._guess_letter(inp)
        self.log(inp)

    def _guess_word(self, word):
        if self.word == word:
            self.guessed = True
        else:
            self.lives -=1
    
    def _guess_letter(self, letter):
        # Check if the letter hasn't been tried
        if letter not in self.letters_tried:
            self.letters_tried.append(letter)
        
        # Check if lives should be subtracted
        if letter not in self.word:
            self.lives -= 1

        # Check if the word is guessed
        if not any(set(self.word) - set(self.letters_tried)):
            self.guessed = True

    def get_masked_word(self):
        unmask = set(self.word) & set(self.letters_tried)
        return ' '.join([letter if letter in unmask else '_' for letter in self.word])
    
    def log(self, inp, console=True):
        now = datetime.now()
        lives = self.lives
        # TODO: change to hours
        now_str = now.strftime("%Y-%m-%d, %H:%M:%S")
        entry = json.dumps({
            'time':now_str, 
            'lives':lives, 
            'input':inp, 
            'is_guessed':str(self.is_guessed()),
            'tried_letters': str(self.letters_tried),
            'word': self.word
            })

        # Add log entry
        with open('logs.json', 'a') as f:
            f.write(entry)
            f.write('\n')

        if console:
            print("*"*5)
            print(entry)
            print("*"*5)

    def get_word(self):
        return self.word

    def get_lives(self):
        return self.lives

    def is_guessed(self):
        """Check if the word is guessed"""
        return self.guessed

    def is_dead(self):
        """Check if you still have lives as boolean"""
        if self.lives == 0:
            return True
        else: return False

    @staticmethod
    def get_random_word(f_path):
        """Get a random word from a file of words
        
        """
        with open(f_path, 'r') as f:
            text = f.read()
            words = text.split('\n')
            return random.choice(words)

            
if __name__ == '__main__':
    # Tests
    word = Hangman(5)
    word.word = "generators"
    word.guess('a')
    word.guess('e')
    word.guess('o')

    print("=" * 50)
    print("Get word: " + word.get_word())
    print("Get masked word: " + word.get_masked_word())
    print("=" * 50)


    print("Get word: " + word.get_word())
    print("Get masked word: " + word.get_masked_word())
    word.guess('g')
    word.guess('r')
    word.guess('t')
    print("Get masked word: " + word.get_masked_word())
    word.guess('s')
    print("Get masked word: " + word.get_masked_word())
    print("Check the guessed attribute: " + str(word.is_guessed()))
    word.guess('n')
    print("Get masked word: " + word.get_masked_word())
    print("Check the guessed attribute: " + str(word.is_guessed()))

    word2 = Hangman(5)
    word2.word = "confiscate"
    word2.guess('a')
    word2.guess('c')
    word2.guess('confiscate')
