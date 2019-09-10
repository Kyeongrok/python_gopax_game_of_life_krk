import curses
import time

__version_info__ = (0, 0, 2)
__version__ = ".".join(map(str, __version_info__))

class GameOfLife():
    def __init__(self):
        print("init")
        self.screen = curses.initscr()
        self.screen.addstr(5, 5, "hello")
        self.screen.refresh()
        time.sleep(3)



def main():
    print("gameoflife of life start")
    game = GameOfLife()

if __name__ == "__main__":
    main()
