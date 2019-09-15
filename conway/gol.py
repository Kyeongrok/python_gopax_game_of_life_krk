import curses
import time
from curses import textpad

class GameOfLife():

    grid = []
    generations = 0

    def __init__(self, num_rows, num_cols):
        self.stdscr = curses.initscr()
        self.grid = self.make_init_grid(num_rows, num_cols)

        # 입력받은 점을 찍는다
        # [(), (), ()] 형태로 받는다.
        self.grid[2][3] = 1
        self.grid[3][4] = 1
        self.grid[4][2] = 1
        self.grid[4][3] = 1
        self.grid[4][4] = 1


    def make_init_grid(self, max_rows, max_columns):
        grid = [[0] * max_rows for i in range(max_columns)]
        return grid

    def get_next(self):
        num_rows = len(self.grid)
        num_cols = len(self.grid[0])
        next = [[0] * num_rows for i in range(num_cols)]

        for i in range(num_rows):
            for j in range(num_cols):
                state = self.grid[i][j]
                if (i == 0 or i == num_cols - 1 or j == 0 or j == num_rows - 1):
                    next[i][j] = state
                else:
                    neighbors = self.count_neighbor_cells(self.grid, i, j)
                    if (state == 0 and neighbors == 3):
                        next[i][j] = 1
                    elif (state == 1 and (neighbors < 2 or neighbors > 3)):
                        next[i][j] = 0
                    else:
                        next[i][j] = state
        return next

    def count_neighbor_cells(self, grid, x, y):
        sum = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                sum += grid[x + i][y + j]
        sum -= grid[x][y]
        return sum

    def draw(self):
        # grid를 화면에 출력한다
        self.stdscr.clear()
        self.draw_outter()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    self.stdscr.addstr(i, j, "+")
        self.stdscr.refresh()

    def draw_outter(self):
        h = len(self.grid)
        w = len(self.grid[0])
        box = [
            [0,0],
            [10, 10]
        ]

        textpad.rectangle(self.stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    def start(self):
        print("start")
        while True:
            self.draw()
            time.sleep(0.1)
            self.grid = self.get_next()

