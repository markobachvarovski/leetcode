from random import randint


class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.reverse_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            move = 1
        else:
            move = -1

        self.rows[row] += move
        self.cols[col] += move

        if row == col:
            self.diagonal += move
        if row + col == self.size - 1:
            self.reverse_diagonal += move

        if abs(self.rows[row]) == self.size or abs(self.cols[col]) == self.size or abs(
                self.diagonal) == self.size or abs(self.reverse_diagonal) == self.size:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
