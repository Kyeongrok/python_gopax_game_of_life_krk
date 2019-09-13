import curses
from curses import textpad

def main(stdscr):
    h, w = stdscr.getmaxyx()

    box = [[3,3], [h-3, w-3]]

    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)

