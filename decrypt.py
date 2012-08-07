#!/usr/bin/env python
import curses
import time
import sys
import fileinput
import random
import string

lines = []

for line in fileinput.input():
    lines.append(line)
fileinput.close()

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
confirmed_per_line = [[] for line in lines]
chance = 0.01
while True:
    still_random = 0
    chance += 0.01
    screen.erase()
    (x,y) = screen.getmaxyx()
    for line_num in range(min(len(lines), y-1)):
        line = lines[line_num]
        for i in [i  for i in range(len(line)) if i not in confirmed_per_line[line_num]]:
            still_random += 1
            if random.random() < chance:
                confirmed_per_line[line_num].append(i)
        random_line = ''.join(random.choice(string.ascii_uppercase + string.digits) if x not in confirmed_per_line[line_num] else line[x] for x in range(len(line)))
        try:
            screen.addstr(line_num, 0, random_line)
        except Exception:
            pass

    screen.refresh()
    time.sleep(0.1)
    if still_random < 1:
        break
time.sleep(2)
curses.endwin()

