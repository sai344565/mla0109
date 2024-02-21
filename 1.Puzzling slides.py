class SlidingPuzzle:
    def __init__(self, initial_state):
        self.board = initial_state
        self.size = len(initial_state)
    def display(self):
        for row in self.board:
            print(row)
    def find_empty_space(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return i, j
    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size
    def swap_empty_space(self, new_row, new_col):
        empty_row, empty_col = self.find_empty_space()
        self.board[empty_row][empty_col], self.board[new_row][new_col] = self.board[new_row][new_col], 0
    def move_up(self):
        empty_row, empty_col = self.find_empty_space()
        if self.is_valid_move(empty_row - 1, empty_col):
            self.swap_empty_space(empty_row - 1, empty_col)
    def move_down(self):
        empty_row, empty_col = self.find_empty_space()
        if self.is_valid_move(empty_row + 1, empty_col):
            self.swap_empty_space(empty_row + 1, empty_col)
    def move_left(self):
        empty_row, empty_col = self.find_empty_space()
        if self.is_valid_move(empty_row, empty_col - 1):
            self.swap_empty_space(empty_row, empty_col - 1)
    def move_right(self):
        empty_row, empty_col = self.find_empty_space()
        if self.is_valid_move(empty_row, empty_col + 1):
            self.swap_empty_space(empty_row, empty_col + 1)
initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
puzzle = SlidingPuzzle(initial_state)
print("Initial State:")
puzzle.display()
puzzle.move_down()
print("\nAfter moving down:")
puzzle.display()
puzzle.move_right()
print("\nAfter moving right:")
puzzle.display()
