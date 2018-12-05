import sys


def _read_files():
    ids = []
    input_file = sys.argv[1]
    with open(input_file, 'r') as fp:
        for x in fp:
            ids.append(str(x))
    return ids


rows = _read_files()
fabric = [[0 for x in range(1000)] for y in range(1000)]

# 3 @ 5,5: 2x2
pattern = r'#(\d*) @ (\d*),(\d*): (\d*)x(\d*)'
import re
from collections import namedtuple

Design = namedtuple('Design', ['id', 'left', 'top', 'width', 'height'])
values = []
for row in rows:
    matches = re.match(pattern, row)
    values.append(Design(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)), int(matches.group(4)),
                         int(matches.group(5))))

for design in values:
    for x in range(design.left, design.left+design.width):
        for y in range(design.top, design.top+design.height):
            try:
                fabric[x][y] += 1
            except:
                print(f'{design}')

overlaps = 0
for x in range(1000):
    for y in range(1000):
        if fabric[x][y] >= 2:
            overlaps += 1
print(f'{overlaps} overlaps')

# print(fabric)


def is_intact(design):
    for x in range(design.left, design.left+design.width):
        for y in range(design.top, design.top+design.height):
            if fabric[x][y] == 1:
                continue
            else:
                return None
    return design

for design in values:
    state = is_intact(design)
    if state:
        print(state)