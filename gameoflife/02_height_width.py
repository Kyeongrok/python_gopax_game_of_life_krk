import curses
import time
from curses import textpad


def main(stdscr):
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()

    box = [
        [1,1],
        [h-2, w-2]
    ]

    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.addstr(0, 0, str(h))
    stdscr.addstr(1, 0, str(w))

    stdscr.addstr(19, 19, "0")
    stdscr.addstr(20, 18, "0")
    stdscr.addstr(20, 19, "0")
    stdscr.addstr(20, 20, "0")
    stdscr.addstr(21, 19, "0")
    stdscr.refresh()

    time.sleep(3)
    stdscr.addstr(19, 19, "1")
    stdscr.addstr(20, 18, "1")
    stdscr.addstr(20, 19, "1")

    stdscr.getch()

curses.wrapper(main)

