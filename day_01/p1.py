from collections import Counter


def part_1():
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    dist = 0
    for l, r in zip(sorted_left, sorted_right):
        dist += abs(l - r)

    print("Part 1:", dist)
    assert dist == 1319616


def part_2():
    counter = Counter(right_list)
    score = 0

    for l in left_list:
        times = counter[l]
        score += l * times

    print("Part 2:", score)
    assert score == 27267728


if __name__ == "__main__":
    left_list = []
    right_list = []

    with open("input.txt") as f:
        for line in f:
            l, r = line.split()
            left_list.append(int(l))
            right_list.append(int(r))

    part_1()
    part_2()
