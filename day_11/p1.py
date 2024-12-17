def blink(stones: list[int]):
    new = []
    for n in stones:
        if n == 0:
            new.append(1)

        elif len(str(n)) % 2 == 0:
            n_digits = len(str(n))
            left, right = str(n)[: n_digits // 2], str(n)[n_digits // 2 :]
            new.append(int(left))
            new.append(int(right))

        elif len(str(n)) % 2 == 1:
            new.append(n * 2024)

    return new


with open("input.txt") as f:
    for line in f:
        line_of_stones = [int(n) for n in line.strip().split()]
        break

for blink_number in range(1, 26):
    line_of_stones = blink(line_of_stones)
    print(blink_number, ": ", len(line_of_stones))

assert len(line_of_stones) == 184927

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, line_of_stones)))
