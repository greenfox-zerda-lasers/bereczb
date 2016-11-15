import rand_word
import os
import draw

class Game:

    def __init__(self):
        self.start()

    def start(self):
        self.chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.guesses = []
        self.num_of_fails = 0
        self.used_chars = ''
        self.word = rand_word.random_word()
        self.players_word = list('-' * len(self.word))
        self.game_loop()

    def game_loop(self):
        while self.num_of_fails < 7:
            self.update_scr()

            # print(self.word, self.print_players_word())
            self.guess()
            if len(self.players_guess) > 1:
                if self.players_guess == self.word:
                    self.players_word = list(self.players_guess)
                    self.update_scr()
                    print('\n', '\n', 'congrats!!')
                    break
                else:
                    print('wrong guess!!')
                    print('my word: ', self.word)
                    break
            self.used_chars += self.players_guess + ' '
            if self.players_guess in self.word and self.players_guess not in self.players_word:
                self.update_players_word()

                if self.word == self.print_players_word():
                    self.update_scr()
                    print('congrats!!')
                    break
            else:
                self.num_of_fails += 1

            self.update_scr()
            print('my word: ', self.word)

    def print_players_word(self):
        self.result = ''
        for i in range(len(self.players_word)):
            self.result += self.players_word[i]
        return self.result

    def update_players_word(self):
        for i in range(len(self.players_word)):
            if self.word[i] == self.players_guess:
                self.players_word[i] = self.players_guess

    def update_scr(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.draw_man(self.num_of_fails)
        print('used characters: ',self.used_chars)
        # print(self.word)
        print('\n',self.print_players_word(), '\n')
        # print(self.num_of_fails, 'failures')

    def draw_man(self, step):
        draw.hangman_graphic(step)

    def guess(self):
        self.players_guess = input('What is your guess?  ')

guess_game = Game()
