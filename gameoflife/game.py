import curses
import time

__version_info__ = (0, 0, 2)
__version__ = ".".join(map(str, __version_info__))

class GameOfLife():
    def drawOutterSquare(self):
        print("kkkkk")
        self.win.addstr(0, 0, "------", curses.COLOR_YELLOW)
        self.screen.refresh()

    def __init__(self):
        print("init")
        self.screen = curses.initscr()
        self.win = curses.newwin(40, 40, 0, 0)
        self.win.border(2)
        self.drawOutterSquare()
        time.sleep(3)



def main():
    print("gameoflife of life start")
    game = GameOfLife()

if __name__ == "__main__":
    main()
