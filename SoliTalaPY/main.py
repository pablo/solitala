import copy
from xmlrpc.client import Boolean
from datetime import datetime

SZ = 7

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
            for i in range(SZ):
                for j in range(SZ):
                    bit = i*SZ + j
                    if SoliTalaBoard.valid_cell(i, j):
                        if ((1 << bit) & value) > 0:
                            self.board[i][j] = 1
                        else:
                            self.board[i][j] = 0
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
        for i in range(SZ):
            for j in range(SZ):
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
        for i in range(SZ):
            for j in range(SZ):
                if SoliTalaBoard.valid_cell(i, j):
                    if self.board[i][j] == 0:
                        # check for valid moves on empty cells
                        ## left
                        if SoliTalaBoard.valid_cell(i-2, j) and SoliTalaBoard.valid_cell(i-1, j):
                            if self.board[i-2][j] == 1 and self.board[i-1][j] == 1:
                                bc = copy.deepcopy(self.board)
                                bc[i-2][j] = 0
                                bc[i-1][j] = 0
                                bc[i][j] = 1
                                ret.append(SoliTalaBoard.board_val(bc))
                        ## top
                        if SoliTalaBoard.valid_cell(i, j-2) and SoliTalaBoard.valid_cell(i, j-1):
                            if self.board[i][j-2] == 1 and self.board[i][j-1] == 1:
                                bc = copy.deepcopy(self.board)
                                bc[i][j-2] = 0
                                bc[i][j-1] = 0
                                bc[i][j] = 1
                                ret.append(SoliTalaBoard.board_val(bc))
                        ## right
                        if SoliTalaBoard.valid_cell(i+2, j) and SoliTalaBoard.valid_cell(i+1, j):
                            if self.board[i+2][j] == 1 and self.board[i+1][j] == 1:
                                bc = copy.deepcopy(self.board)
                                bc[i+2][j] = 0
                                bc[i+1][j] = 0
                                bc[i][j] = 1
                                ret.append(SoliTalaBoard.board_val(bc))
                        ## bottom
                        if SoliTalaBoard.valid_cell(i, j+2) and SoliTalaBoard.valid_cell(i, j+1):
                            if self.board[i][j+2] == 1 and self.board[i][j+1] == 1:
                                bc = copy.deepcopy(self.board)
                                bc[i][j+2] = 0
                                bc[i][j+1] = 0
                                bc[i][j] = 1
                                ret.append(SoliTalaBoard.board_val(bc))
        return ret


    @staticmethod
    def valid_cell(x, y) -> bool:
        if x < 2:
            return 2 <= y <= 4
        elif x <= 4:
            return 0 <= y <= 6
        elif x <= 6:
            return 2 <= y <= 4
        else:
            return False

    def print_board(self):
        for i in range(SZ):
            for j in range(SZ):
                if SoliTalaBoard.valid_cell(i, j):
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

class SoliTalaSolver:

    def __init__(self):
        pass

    def do_solve(self):
        self.solve(STARTING_BOARD.valid_moves(), [STARTING_BOARD,], 0)

    def solve(self, valid_moves: list = None, boards: list = None, depth: int = 0):
        global iter
        iter += 1
        if iter%10000 == 0:
            print(f"{datetime.now()} -> Current depth {depth} on iter {iter}")
        if iter > 100000:
            print("BYE for now!")
            return
        for board_val in valid_moves:
            current_board = SoliTalaBoard(board_val)
            boards.append(current_board)
            if board_val == WINNING_BOARD_VAL:
                print("I FOUND IT!!!!")
                for board in boards:
                    board.print_board()
                    print("==============")
                return True
            else:
                self.solve(current_board.valid_moves(), boards, depth+1)
                boards.pop()


solver = SoliTalaSolver()
solver.do_solve()