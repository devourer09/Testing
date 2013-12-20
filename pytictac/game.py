"""This module contains the logic for tic tac toe."""

import random
import time

class Board:
    def __init__(self, board_size=3):
        self.location_values = (' ', 'X', 'O')
        self.location = []
        self.turn = 0

        random.seed(int(time.time()))

        for i in range(board_size):
            self.location.append([])
            for j in range(board_size):
                self.location[i].append(' ')

    def print_board(self, board=''):
        print()
        if board == '':
            board = self.location
        for i, ii in enumerate(reversed(board)):
            if i == 0:
                print("  -------------")
            for j, jj in enumerate(ii):
                if j == 0:
                    print(len(board)-1-i, end='')
                print(" | ", end='')
                print(jj, end='')
                if j == len(ii)-1:
                    print(" |")
            print("  -------------")
        print("    0   1   2")

    def populate(self):
        for i, ii in enumerate(self.location):
            for j, jj in enumerate(ii):
                self.location[i][j] = self.location_values[random.randint(0, len(self.location_values)-1)]

    def rotate(self):
        self.location = list(zip(*reversed(self.location)))

    def mark(self, location):
        if self.turn % 2:
            player_mark = 'o'
        else:
            player_mark = 'x'

        self.location[location[0]][location[1]] = player_mark
        self.turn += 1

    def is_winner(self):
        for i in self.location:
            for j in i:
                pass

    def touching_same(self):
        pass
