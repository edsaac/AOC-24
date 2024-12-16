from dataclasses import dataclass
from itertools import cycle
from collections import Counter


@dataclass
class Point:
    row: int
    col: int

    def __add__(self, other):
        return Point(self.row + other.row, self.col + other.col)

    def __hash__(self) -> int:
        return hash((self.row, self.col))


rotations = {
    Point(-1, 0): "up",
    Point(0, 1): "right",
    Point(1, 0): "down",
    Point(0, -1): "left",
}


def find_chapeau(lines: list[str]) -> Point:
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch == "^":
                return Point(row, col)


with open("input.txt") as f:
    the_map = f.readlines()


the_map = [[*(line.strip())] for line in the_map]
xsize, ysize = len(the_map[0]), len(the_map)
cl_rot = cycle(rotations)


@dataclass
class Walker:
    loc: Point
    direction = next(cl_rot)
    steps: int = 0

    def advance(self):
        obstacle = the_map[self.one_step_ahead.row][self.one_step_ahead.col]

        while obstacle == "#":
            print("Found a wall!")
            the_map[self.loc.row][self.loc.col] = "+"

            self.direction = next(cl_rot)
            obstacle = the_map[self.one_step_ahead.row][self.one_step_ahead.col]

        self.loc += self.direction
        self.steps += 1

        path = "|" if rotations[self.direction] in ("up", "down") else "-"
        the_map[self.loc.row][self.loc.col] = path

    def is_ahead_outside(self):
        return (
            self.one_step_ahead.col < 0
            or self.one_step_ahead.col >= ysize
            or self.one_step_ahead.row < 0
            or self.one_step_ahead.row >= xsize
        )

    @property
    def one_step_ahead(self):
        return self.loc + self.direction

    def __str__(self) -> str:
        return f"{self.loc}, {self.direction}, {self.steps}"


guard = Walker(
    starting := find_chapeau(the_map),
)


while True:
    if guard.is_ahead_outside():
        break

    print("---")
    print("Current location:", guard.loc)
    print("Current direction:", rotations[guard.direction])
    guard.advance()


as_string = "".join(["".join(row) for row in the_map])
count = Counter(as_string)


with open("output.txt", "w") as f:
    for row in the_map:
        f.write("".join(row) + "\n")

print(spots := count["-"] + count["|"] + count["+"] + count["^"])
assert spots == 5312
