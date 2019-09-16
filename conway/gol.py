import curses
import time
from curses import textpad

class GameOfLife():

    grid = []
    generations = 0
    state = "waiting"

    def __init__(self, num_rows, num_cols, points):
        self.stdscr = curses.initscr()
        self.stdscr.keypad(1)
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        self.height = max(40, num_rows)
        self.width = max(80, num_cols)
        self.win = curses.newwin(self.height, self.width, 0, 0)
        self.win.nodelay(1)
        # self.win.move(1, 1)
        self.grid = [[0] * self.width for i in range(self.height)]
        self.draw_info()

        # 입력받은 점을 찍는다
        for point in points:
            self.grid[point["x"]][point["y"]] = 1

    def get_next(self):
        num_rows = self.height
        num_cols = self.width
        next = [[0] * num_cols for i in range(num_rows)]

        for i in range(num_rows):
            for j in range(num_cols):
                state = self.grid[i][j]
                # print(num_cols, num_rows)
                if (i == 0 or i == num_rows - 1 or j == 0 or j == num_cols - 1):
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
                # print(x, y, i, j)
                sum += grid[x + i][y + j]
        sum -= grid[x][y]
        return sum

    def draw_info(self):
        self.win.box()
        self.win.addstr(2, self.height - 21, "generations: {}".format(self.generations))
        self.win.addstr(3, self.height - 21, "s: start    q: quit")

    def draw(self):
        # grid를 화면에 출력한다
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 1:
                    self.win.addch(i, j, "+")
        self.win.refresh()

    def start(self):
        print("start")
        self.state = "running"
        while self.state == "running":
            self.win.clear()
            self.generations += 1
            self.draw_info()
            self.draw()
            time.sleep(0.1)
            self.grid = self.get_next()
            key = self.win.getch()
            if key == ord("q"):
                exit()

