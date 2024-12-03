import re

PATTERN = re.compile(r"mul\([\d]{1,3},[\d]{1,3}\)")


def extract_mults(string: str):
    matches = re.findall(PATTERN, string)

    acusum = 0

    for match in matches:
        x, y = match.replace("mul(", "").replace(")", "").split(",")
        x = int(x)
        y = int(y)

        acusum += x * y

    return acusum


def part_01():
    acusum = extract_mults(memory)
    print("Part 1: ", acusum)
    assert acusum == 175700056


def part_02():
    instruction = re.compile(r"do(?:n't)?\(\)")
    matches = re.finditer(instruction, memory)

    prev = "do()"
    span = 0
    acusum = 0

    for match in matches:
        if prev == "do()":
            acusum += extract_mults(memory[span : match.end(0)])

        span = match.end(0)
        prev = match[0]

    print("Part 2: ", acusum)
    assert acusum == 71668682


if __name__ == "__main__":
    with open("input.txt") as f:
        memory = f.readlines()
        memory = "".join(memory)

    # part_01()
    part_02()
