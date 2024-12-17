from dataclasses import dataclass
import numpy as np


@dataclass
class Coordinate:
    x: int
    y: int

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)


@dataclass
class Arcade:
    a: Coordinate
    b: Coordinate
    prize: Coordinate

    def __post_init__(self):
        self.coeff = np.array(
            [
                [self.a.x, self.b.x],
                [self.a.y, self.b.y],
            ]
        )

    @property
    def det(self):
        return np.linalg.det(self.coeff)

    @property
    def solution(self):
        if self.det != 0:
            return np.linalg.solve(self.coeff, np.array([self.prize.x, self.prize.y]))
        return np.array([-1, -1])

    @property
    def is_int(self):
        if np.any(self.solution < 0):
            return False
        return all(abs(round(x) - x) < 1e-6 for x in self.solution)


arcades = []

with open("input.txt") as f:
    for line in f:
        if line.strip():
            button_or_prize, data = line.split(":")
            sep = "+" if "Button" in button_or_prize else "="
            values = Coordinate(
                *(map(int, (rule.strip().split(sep)[-1] for rule in data.split(","))))
            )
            if "Button A" in button_or_prize:
                button_a = values
            elif "Button B" in button_or_prize:
                button_b = values
            elif "Prize" in button_or_prize:
                prize = values

        else:
            arcades.append(Arcade(button_a, button_b, prize))

total = 0
for i, arcade in enumerate(arcades):
    subtot = arcade.is_int * ((3 * arcade.solution[0]) + arcade.solution[1])
    total += subtot

print(f"Total: {total}")
