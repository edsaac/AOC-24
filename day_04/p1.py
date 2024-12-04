with open("input.txt") as f:
    lines = f.readlines()
    array = [[*(c.strip())] for c in lines]


def test_right(i, j):
    if j + 4 > len(array[i]):
        return False

    subsample = "".join(array[i][j : j + 4])
    if subsample == "XMAS":
        return True
    return False


def test_left(i, j):
    if j - 3 < 0:
        return False

    subsample = ("".join(array[i][j - 3 : j + 1]))[::-1]
    if subsample == "XMAS":
        return True
    return False


def test_up(i, j):
    if i - 3 < 0:
        return False

    subsample = "".join([array[ix][j] for ix in range(i, i - 4, -1)])

    if subsample == "XMAS":
        return True
    return False


def test_down(i, j):
    if i + 4 > len(array):
        return False

    subsample = "".join([array[ix][j] for ix in range(i, i + 4)])

    if subsample == "XMAS":
        return True
    return False


def diagonal_down_right(i, j):
    if j + 4 > len(array[i]):
        return False

    if i + 4 > len(array):
        return False

    subsample = "".join(
        [array[ix][jy] for ix, jy in zip(range(i, i + 4), range(j, j + 4))]
    )

    if subsample == "XMAS":
        return True
    return False


def diagonal_down_left(i, j):
    if j - 3 < 0:
        return False

    if i + 4 > len(array):
        return False

    subsample = "".join(
        [array[ix][jy] for ix, jy in zip(range(i, i + 4), range(j, j - 4, -1))]
    )

    if subsample == "XMAS":
        return True
    return False


def diagonal_up_right(i, j):
    if j + 4 > len(array[i]):
        return False

    if i - 3 < 0:
        return False

    subsample = "".join(
        [array[ix][jy] for ix, jy in zip(range(i, i - 4, -1), range(j, j + 4))]
    )

    if subsample == "XMAS":
        return True
    return False


def diagonal_up_left(i, j):
    if j - 3 < 0:
        return False

    if i - 3 < 0:
        return False

    subsample = "".join(
        [array[ix][jy] for ix, jy in zip(range(i, i - 4, -1), range(j, j - 4, -1))]
    )

    if subsample == "XMAS":
        return True
    return False


def check_all_directions(i, j):
    return int(
        test_right(i, j)
        + test_left(i, j)
        + diagonal_down_right(i, j)
        + diagonal_down_left(i, j)
        + diagonal_up_right(i, j)
        + diagonal_up_left(i, j)
        + test_up(i, j)
        + test_down(i, j)
    )


def part_01():
    counter = 0

    for i, line in enumerate(array):
        for j, char in enumerate(line):
            if char == "X":
                print(i, ",", j, ">>", n := check_all_directions(i, j))
                # print("to the right:", test_right(i, j))
                # print("to the left:", test_left(i, j))
                # print("going up:", test_up(i, j))
                # print("going down:", test_down(i, j))
                # print("diagonal down right:", diagonal_down_right(i, j))
                # print("diagonal down left:", diagonal_down_left(i, j))
                # print("diagonal up right:", diagonal_up_right(i, j))
                # print("diagonal up left:", diagonal_up_left(i, j))
                counter += n

    print("Part 1:", counter)
    assert counter == 2639


if __name__ == "__main__":
    part_01()
