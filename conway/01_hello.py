import curses
import time

stdscr = curses.initscr()
stdscr.addstr(5, 5, "Hello")
stdscr.refresh()
time.sleep(3)

curses.endwin()