from dataclasses import dataclass
from functools import reduce
from operator import add

import matplotlib.pyplot as plt

x_lim = 101
y_lim = 103

field = [[0 for j in range(x_lim)] for _ in range(y_lim)]


def interesting_field():
    add_rows = [reduce(add, row) for row in field]
    return max(add_rows) > 20


def print_field(title: str):
    fig, ax = plt.subplots()
    ax.imshow(field)
    fig.savefig(f"frames/{title}.png")
    plt.close(fig)
    # for row in field:
    #     print(" ".join([f"{x}" if x > 0 else "•" for x in row]))
    # print(" ")


def reset_field():
    global field
    field = [[0 for j in range(x_lim)] for _ in range(y_lim)]


@dataclass
class Robot:
    position: complex
    velocity: complex

    def move(self):
        self.position += self.velocity
        x = self.position.real % x_lim
        y = self.position.imag % y_lim

        self.position = complex(x, y)

    def move_n_times(self, n: int = 100):
        for _ in range(n):
            self.move()
        print(f"Moved {n} times")

    def show_in_field(self):
        global field
        xcord = int(self.position.real)
        ycord = int(self.position.imag)

        field[ycord][xcord] += 1

    @property
    def quadrant(self):
        x = self.position.real
        y = self.position.imag

        lim_x = x_lim // 2
        lim_y = y_lim // 2

        if x == lim_x or y == lim_y:
            return "Middle"
        elif x < lim_x and y < lim_y:
            return "Top Left"
        elif x < lim_x and y > lim_y:
            return "Top Right"
        elif x > lim_x and y < lim_y:
            return "Bottom Left"
        elif x > lim_x and y > lim_y:
            return "Bottom Right"

        raise ValueError("Invalid position")


robots = []
with open("input.txt") as f:
    for line in f:
        p, v = line.split(" ")

        # Parse position
        p = complex(*map(int, p.split("=")[-1].split(",")))

        # parse velocity
        v = complex(*map(int, v.split("=")[-1].split(",")))

        robots.append(Robot(p, v))

t = 0
while True:
    for robot in robots:
        robot.move()
        robot.show_in_field()

    t += 1

    if interesting_field():
        print_field(title=f"Time {t}")

    reset_field()

    if t % 100 == 0:
        print("Time ", t)

    if t > 1_000_000:
        break
