#!/usr/bin/env python
import curses
import time
import fileinput
import random
import string

lines = []
chance = 0.1
confirmed_per_line = []


screen = curses.initscr()
curses.noecho()
try:
    curses.curs_set(0)
except:
    pass
screen.keypad(1)

def iterate(increase = False):
    still_random = 0
    global chance, confirmed_per_line, lines
    if increase:
        chance += 0.01
    screen.erase()
    (y,x) = screen.getmaxyx()
    final_line = len(lines)
    if final_line > y:
        first_line = final_line - y
    else:
        first_line = 0
    for line_num in range(first_line, final_line):
        line = lines[line_num]
        for i in [i  for i in range(min(x, len(line))) if i not in confirmed_per_line[line_num]]:
            still_random += 1
            if random.random() < chance:
                confirmed_per_line[line_num].append(i)
        random_line = ''.join(random.choice(string.punctuation) if col not in confirmed_per_line[line_num] else line[col] for col in range(min(len(line), x)))
        try:
            screen.addstr(line_num - first_line, 0, random_line)
        except Exception:
            pass

    screen.refresh()
    time.sleep(0.1)
    return still_random > 0

try:
    for line in fileinput.input():
        confirmed_per_line.append([])
        lines.append(line.rstrip())
        iterate()
    fileinput.close()
    while iterate(True):
        pass
    time.sleep(2)
finally:
    curses.endwin()
for line in lines:
    print(line)
