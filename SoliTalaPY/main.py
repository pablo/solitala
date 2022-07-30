import sys
from datetime import datetime

SZ = 7


def valid_cell(x, y) -> bool:
    if x < 2:
        return 2 <= y <= 4
    elif x <= 4:
        return 0 <= y <= 6
    elif x <= 6:
        return 2 <= y <= 4
    else:
        return False


VALID_CELLS = []


for i in range(SZ):
    for j in range(SZ):
        if valid_cell(i, j):
            VALID_CELLS.append((i, j))


class SoliTalaBoard:

    def __init__(self, value: int = 0):
        """
        Get a board from its representing int value
        :param value: int value represeting game's board according to
        agreed enumeration
        """
        #self.board = [[0]*SZ]*SZ
        self.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        if value > 0:
            for vcell in VALID_CELLS:
                i, j = vcell
                bit = i*SZ + j
                if ((1 << bit) & value) > 0:
                    self.board[i][j] = 1
                else:
                    self.board[i][j] = 0

    @classmethod
    def from_board(cls, board: list):
        ret = SoliTalaBoard()
        ret.board = board
        return ret

    @staticmethod
    def board_val(board: list) -> int:
        """
        Gets int value that represents the board
        :return: int value that represents the board
        """
        val = 0
        for vcell in VALID_CELLS:
            i, j = vcell
            if board[i][j] != 0:
                bit = i*SZ + j
                val += (1 << bit)
        return val

    def to_val(self) -> int:
        return SoliTalaBoard.board_val(self.board)

    def is_winning(self) -> bool:
        """
        Returns  true if board is a winning position
        """
        return self.to_val() == WINNING_BOARD_VAL

    def valid_moves(self) -> list:
        """
        Calculates valid moves from current's board
        :return: a list of ints representing board with valid next
        moves with respect to current board
        """
        ret = []
        for vcell in VALID_CELLS:
            i, j = vcell
            if self.board[i][j] == 0:
                # check for valid moves on empty cells
                ## left
                if i-2 > 0 and self.board[i-2][j] == 1 and self.board[i-1][j] == 1:
                    self.board[i-2][j] = 0
                    self.board[i-1][j] = 0
                    self.board[i][j] = 1
                    ret.append(self.to_val())
                    self.board[i-2][j] = 1
                    self.board[i-1][j] = 1
                    self.board[i][j] = 0
                ## top
                if j-2 >= 0 and self.board[i][j-2] == 1 and self.board[i][j-1] == 1:
                    self.board[i][j-2] = 0
                    self.board[i][j-1] = 0
                    self.board[i][j] = 1
                    ret.append(self.to_val())
                    self.board[i][j-2] = 1
                    self.board[i][j-1] = 1
                    self.board[i][j] = 0
                ## right
                if i+2 < SZ and self.board[i+2][j] == 1 and self.board[i+1][j] == 1:
                    self.board[i+2][j] = 0
                    self.board[i+1][j] = 0
                    self.board[i][j] = 1
                    ret.append(self.to_val())
                    self.board[i+2][j] = 1
                    self.board[i+1][j] = 1
                    self.board[i][j] = 0
                ## bottom
                if j+2 < SZ and self.board[i][j+2] == 1 and self.board[i][j+1] == 1:
                    self.board[i][j+2] = 0
                    self.board[i][j+1] = 0
                    self.board[i][j] = 1
                    ret.append(self.to_val())
                    self.board[i][j+2] = 1
                    self.board[i][j+1] = 1
                    self.board[i][j] = 0
        return ret

    def print_board(self):
        for i in range(SZ):
            for j in range(SZ):
                if valid_cell(i, j):
                    if self.board[i][j] == 1:
                        print("X", end=' ')
                    else:
                        print(" ", end=' ')
                else:
                    print("#", end=' ')
            print("")


INITIAL_BOARD = SoliTalaBoard.from_board([
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0]
])

EASY_BOARD = SoliTalaBoard.from_board([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

WINNING_BOARD = SoliTalaBoard.from_board([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

WINNING_BOARD_VAL = WINNING_BOARD.to_val()

STARTING_BOARD = INITIAL_BOARD

iter = 0
solutions = 0

class SoliTalaSolver:

    def __init__(self):
        pass

    def do_solve(self):
        self.solve(STARTING_BOARD.valid_moves(), [STARTING_BOARD,], 0)

    def solve(self, valid_moves: list = None, boards: list = None, depth: int = 0):
        global iter, solutions
        iter += 1
        if iter%100000 == 0:
            print(f"{datetime.now()} -> Current depth {depth} on iter {iter} - solutions {solutions}")
        for board_val in valid_moves:
            current_board = SoliTalaBoard(board_val)
            boards.append(current_board)
            if board_val == WINNING_BOARD_VAL:
                solutions += 1
                print(f"I FOUND IT!!!! SOLUTION #{solutions}")
                for board in boards:
                    board.print_board()
                    print("==============")
                sys.exit(0)
            else:
                self.solve(current_board.valid_moves(), boards, depth+1)
                boards.pop()


solver = SoliTalaSolver()
solver.do_solve()
