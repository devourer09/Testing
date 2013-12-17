import game

if __name__ == "__main__":
    b = game.Board()
    b.populate()
    for i in range(4):
        b.print_board()
        b.rotate()
