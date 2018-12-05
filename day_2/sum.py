from collections import Counter
import sys
def _read_files():
    ids = []
    input_file = sys.argv[1]
    with open(input_file, 'r') as fp:
        for x in fp:
            ids.append(str(x))
    return ids


ids = _read_files()
twos = 0
threes = 0
for id in ids:
    count = Counter(list(id))
    values = count.values()
    if 2 in values:
        twos += 1
    if 3 in values:
        threes += 1
print(f'twos = {twos}  three = {threes}')
print(twos*threes)

for (idx, val) in enumerate(ids):
    for (idx2, val2) in enumerate(ids[idx:]):
        # compare 
        # assume len the same
        diffs = 0
        for (idc, c) in enumerate(list(val)):
            if c == val2[idc]:
                continue
            else:
                diffs += 1
            if diffs > 1:
                break
        if diffs == 1:
            print(f'val1 = {val}val2 = {val2}')
