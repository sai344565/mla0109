class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.current_position = (0, 0) 
    def display_grid(self):
        for row in self.grid:
            print(row)
    def move_up(self):
        if self.current_position[0] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])
    def move_down(self):
        if self.current_position[0] < self.rows - 1:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
    def move_left(self):
        if self.current_position[1] > 0:
            self.current_position = (self.current_position[0], self.current_position[1] - 1)
    def move_right(self):
        if self.current_position[1] < self.cols - 1:
            self.current_position = (self.current_position[0], self.current_position[1] + 1)
    def clean_current_cell(self):
        row, col = self.current_position
        if self.grid[row][col] == 'D':
            self.grid[row][col] = 'C'  
    def clean_grid(self):
        while any('D' in row for row in self.grid):
            self.clean_current_cell()
            if self.current_position[1] < self.cols - 1 and self.grid[self.current_position[0]][self.current_position[1] + 1] == 'D':
                self.move_right()
            elif self.current_position[0] < self.rows - 1 and self.grid[self.current_position[0] + 1][self.current_position[1]] == 'D':
                self.move_down()
            elif self.current_position[1] > 0 and self.grid[self.current_position[0]][self.current_position[1] - 1] == 'D':
                self.move_left()
            elif self.current_position[0] > 0 and self.grid[self.current_position[0] - 1][self.current_position[1]] == 'D':
                self.move_up()
grid = [
    ['D', 'C', 'D', 'C'],
    ['D', 'D', 'C', 'D'],
    ['C', 'C', 'C', 'D'],
    ['D', 'D', 'D', 'C']
]
vacuum_cleaner = VacuumCleaner(grid)
print("Initial Grid:")
vacuum_cleaner.display_grid()
vacuum_cleaner.clean_grid()
print("\nCleaned Grid:")
vacuum_cleaner.display_grid()
