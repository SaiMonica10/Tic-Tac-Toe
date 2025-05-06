import random

class TicTacToe:
    def __init__(self):
        self.board = ["-"] * 9
        self.current_player = "X"
        self.winner = None
        self.game_running = True
        self.tie = False  

    def make_move(self, position):
        if self.board[position] == "-" and self.game_running:
            self.board[position] = self.current_player
            self.check_win()
            self.check_tie()
            if self.game_running:
                self.switch_player()
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def computer_move(self):
        if self.current_player == "O" and self.game_running:
            while True:
                pos = random.randint(0, 8)
                if self.board[pos] == "-":
                    self.make_move(pos)
                    break

    def check_win(self):
        b = self.board
        win_positions = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # cols
            [0,4,8], [2,4,6]            # diagonals
        ]
        for pos in win_positions:
            if b[pos[0]] == b[pos[1]] == b[pos[2]] and b[pos[0]] != "-":
                self.winner = b[pos[0]]
                self.game_running = False

    def check_tie(self):
        if "-" not in self.board and self.winner is None:
            self.tie = True
            self.game_running = False
