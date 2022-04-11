
from collections import deque
import logging
from rich.logging import RichHandler
from copy import deepcopy

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)

log = logging.getLogger("rich")

class Line:
    def __init__(self, line_list):
        self.line_list = line_list

    def take(self, amount):
        riders_boarding = []
        if amount > len(self.line_list):
            riders_boarding = self.line_list
            self.line_list = []
        else:
            riders_boarding = self.line_list[:amount]
            self.line_list = self.line_list[amount:]
        return riders_boarding

    def add(self, new_riders):
        self.line_list.extend(new_riders)

    def __bool__(self):
        return bool(self.line_list)

    def __len__(self):
        return len(self.line_list)

class Bench:

    def __init__(self, id, size=2):
        self.count = 0
        self.id = id
        self.riders = []
        self.size = size

    def load(self, riders):
        self.count += len(riders)
        self.riders.extend(riders)

    def unload(self):
        self.count = 0
        riders_temp = self.riders
        self.riders = []
        return riders_temp


class Lift:

    def __init__(self, num_benches, bench_size=2):
        half = num_benches / 2
        self.benches_up = deque()
        self.benches_down = deque()
        for i in range(num_benches):
            if i < half:
                self.benches_up.append(Bench(i, bench_size))
            else:
                self.benches_down.append(Bench(i, bench_size))
        self.bench_size = bench_size

    def people_riding_up(self):
        return any(bench.count for bench in self.benches_up)

    def simulate(self, line):
        results = {"loaded": 0, "unloaded": 0, "num_benches": 0}

        # self.print_lift()
        # Continue to cycle until the line is empty!
        while line:
            self.cycle_bench(line, results)
        # Continue to cycle until everyone is unloaded!
        while self.people_riding_up():
            self.cycle_bench(line, results)
        return results

    def cycle_bench(self, line, results=None):
        results = results or {"loaded": 0, "unloaded": 0, "num_benches": 0}
        # This will be a list of people
        list_of_riders_line = line.take(self.bench_size)

        # load bottom
        bench = self.benches_down.popleft()
        bench.load(list_of_riders_line)
        self.benches_up.append(bench)
        results["loaded"] += len(list_of_riders_line)
        # unload top
        bench = self.benches_up.popleft()
        list_of_riders_unloaded = bench.unload()
        results["unloaded"] += len(list_of_riders_unloaded)
        self.benches_down.append(bench)
        results["num_benches"] += 1

        log.info(f"Loading from Line: {list_of_riders_line}. Unloading from Lift: {list_of_riders_unloaded}")
        # self.print_lift()
        return results
    
    def print_lift(self):
        up_dummy = deepcopy(self.benches_up)
        down_dummy = deepcopy(self.benches_down)
        top_top_line = ""
        top_line = ""
        mid_line = ""
        bottom_line = ""
        for bench in up_dummy:
            width = len(bench.riders) * 5 + 5
            top_top_line +=  f"{bench.id}".center(width, " ")   # " " * (len(bench.riders)//2 * 5 + 2) + f"{i}"
            top_line += "-" * width
            mid_line += f"{bench.riders}".center(width, " ")
            bottom_line += "-" * width

        print("Up Lift:")
        print(top_top_line)
        print(top_line)
        print(mid_line)
        print(bottom_line)


        top_top_line = ""
        top_line = ""
        mid_line = ""
        bottom_line = ""
        
        for bench in down_dummy:
            width = len(bench.riders) * 5 + 5
            top_top_line +=  f"{bench.id}".center(width, " ")   # " " * (len(bench.riders)//2 * 5 + 2) + f"{i}"
            top_line += "-" * width
            mid_line += f"{bench.riders}".center(width, " ")
            bottom_line += "-" * width

        print("Down Lift:")
        print(top_top_line)
        print(top_line)
        print(mid_line)
        print(bottom_line)

def main():
    line = Line(["A", "B", "C", "D", "E"])
    lift = Lift(10)
    results = lift.simulate(line)
    log.info(f"Final Results: {results}")

if __name__ == "__main__":
    main()