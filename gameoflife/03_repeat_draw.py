import curses
import time

grid = []
generations = 0
num_rows = 10
num_cols = 10

def make_init_grid(max_rows, max_columns):
    grid = [[0] * max_rows for i in range(max_columns)]

    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    return grid

def get_next(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    next = [[0] * num_rows for i in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            state = grid[i][j]
            if (i == 0 or i == num_cols - 1 or j == 0 or j == num_rows - 1):
                next[i][j] = state
            else:
                neighbors = count_neighbor_cells(grid, i, j)
                if (state == 0 and neighbors == 3):
                    next[i][j] = 1
                elif (state == 1 and (neighbors < 2 or neighbors > 3)):
                    next[i][j] = 0
                else:
                    next[i][j] = state
    return next

def count_neighbor_cells(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            sum += grid[x + i][y + j]
    sum -= grid[x][y]
    return sum

def draw(stdscr, grid):
    # grid를 화면에 출력한다
    stdscr.clear()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                stdscr.addstr(i, j, "+")
    stdscr.refresh()

def print_grid(grid):
    print("-------------")
    for row in grid:
        print(row)

def main():
    # 알고리즘 적용해서 새 grid를 만듬
    # 화면에 출력함

    stdscr = curses.initscr()
    grid = make_init_grid(num_rows, num_cols)
    # print_grid(grid)

    while True:
        draw(stdscr, grid)
        time.sleep(1)
        grid = get_next(grid)
    # print_grid(grid)


if __name__ == '__main__':
    main()


