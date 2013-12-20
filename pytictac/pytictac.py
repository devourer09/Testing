import game

if __name__ == "__main__":
    b = game.Board()
    #b.populate()

    b.mark((0, 0))
    b.print_board()

    #for i in range(4):
    #    b.print_board()
    #    b.rotate()
