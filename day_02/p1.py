from typing import Self


class Report:
    def __init__(self, report: list[int]) -> None:
        self.report = report

    def all_decreasing(self):
        return all(x < y for x, y in zip(self.report[:-1], self.report[1:]))

    def all_increasing(self):
        return all(x > y for x, y in zip(self.report[:-1], self.report[1:]))

    def all_in_threshold(self):
        for x, y in zip(self.report[:-1], self.report[1:]):
            if not 1 <= abs(x - y) <= 3:
                return False
        return True

    def is_safe(self):
        if self.all_in_threshold():
            if self.all_decreasing() or self.all_increasing():
                return True
        return False

    @classmethod
    def parse_line(cls, line: str) -> Self:
        return cls([int(x) for x in line.split()])


class SubReport(Report):
    def __init__(self, report: Report, ix: int) -> None:
        subreport = report.report.copy()
        del subreport[ix]
        super().__init__(subreport)


def part_01():
    counter = 0
    for report in reports:
        if report.is_safe():
            counter += 1

    print("Part 1: ", counter)
    assert counter == 483


def part_02():
    counter = 0
    for report in reports:
        for i in range(len(report.report)):
            subreport = SubReport(report, i)
            if subreport.is_safe():
                counter += 1
                break

    print("Part 2: ", counter)


if __name__ == "__main__":
    with open("input.txt") as f:
        reports = [Report.parse_line(line) for line in f]

    part_01()
    part_02()
