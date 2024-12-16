from dataclasses import dataclass
from operator import add, mul
from typing import Callable
from itertools import product


@dataclass
class Calibration:
    total: int
    members: list[int]

    def check_combination(self, operations: list[Callable]):
        total = self.members[0]

        for i, operation in zip(self.members[1:], operations):
            total = operation(total, i)

        if self.total == total:
            return True

        return False


calibrations = []

with open("input.txt") as f:
    for line in f:
        tot, elems = line.split(":")
        tot = int(tot.strip())
        elems = [int(n) for n in elems.strip().split()]

        calibrations.append(Calibration(tot, elems))

for calibration in calibrations:
    repeat = len(calibration.members) - 1

    for combo in product((add, mul), repeat=repeat):
        if calibration.check_combination(combo):
            print("Found solution:", calibration.total)

            calibration.possible = True
            break

c = 0
for calibration in calibrations:
    if getattr(calibration, "possible", False):
        c += calibration.total

print(c)
assert c == 4122618559853
