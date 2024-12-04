from collections import Counter, namedtuple

Equis = namedtuple("Equis", ("down_right", "down_left", "up_right", "up_left"))

with open("input.txt") as f:
    lines = f.readlines()
    array = [[*(c.strip())] for c in lines]


def test_for_m_and_s(i, j):
    subset = Equis(
        array[i + 1][j + 1],
        array[i + 1][j - 1],
        array[i - 1][j + 1],
        array[i - 1][j - 1],
    )

    counter = Counter(subset)

    if counter["M"] != 2:
        return False

    if counter["S"] != 2:
        return False

    if subset.down_right == subset.up_left:
        return False

    if subset.down_left == subset.up_right:
        return False

    return True


def part_02():
    counter = 0

    for i, line in enumerate(array[1:-1], start=1):
        for j, char in enumerate(line[1:-1], start=1):
            if char == "A":
                print(i, ",", j, ">>", n := test_for_m_and_s(i, j))
                counter += n

    print("Part 2:", counter)
    assert counter == 2005


if __name__ == "__main__":
    part_02()
