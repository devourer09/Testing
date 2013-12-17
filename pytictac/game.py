import random
import time

class Board:
    def __init__(self):
        self.location_values = ('. ', 'x ', 'o ')
        self.location = []
        random.seed(int(time.time()))
        for i in range(3):
            self.location.append([])
            for j in range(3):
                self.location[i].append('x')

    def print_board(self, board=''):
        print()
        if board == '':
            board = self.location

        for i in board:
            for j in i:
                print(j, end='')
            print()

    def populate(self):
        for i, ii in enumerate(self.location):
            for j, jj in enumerate(ii):
                self.location[i][j] = self.location_values[random.randint(0, 2)]

    def rotate(self):
        self.location = list(zip(*reversed(self.location)))
