from p2 import blink_25_times
from collections import Counter

with open("output.txt") as f:
    for line in f:
        line_of_stones = [int(n) for n in line.strip().split()]
        break

c = Counter(line_of_stones)

for stone in c:
    print(stone, blink_25_times(stone), c[stone])
