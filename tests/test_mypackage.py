import pytest
from mypackage import Line, Bench, Lift
import math


def calculate_cycles_needed(line_length, num_benches, bench_size):
    benches_needed = (line_length // bench_size) + (1 if line_length % bench_size > 0 else 0)
    height_of_lift = math.ceil(num_benches / 2)
    return benches_needed + height_of_lift



def test_line(short_list, long_list):
    line = Line(short_list)
    assert(line.take(4) == short_list)

    line = Line(long_list)
    assert(line.take(4) == ["A", "B", "C", "D"])
    assert(line.take(4) == ["E", "F", "G", "H"])


def test_lift_creation():
    assert(Lift(10) != None)
    with pytest.raises(TypeError) as e_info:
        Lift()

@pytest.mark.lift
@pytest.mark.short
def test_lift_short(short_line):
    num_riders = len(short_line)
    lift = Lift(10)
    results = lift.simulate(short_line)
    assert(results["loaded"] == num_riders)
    assert(results["unloaded"] == num_riders)
    num_benches_used = calculate_cycles_needed(num_riders, 10, 2)
    assert(results["num_benches"] == num_benches_used)

@pytest.mark.lift
@pytest.mark.long
def test_lift_long(long_line):
    num_riders = len(long_line)
    lift = Lift(10)
    results = lift.simulate(long_line)
    assert(results["loaded"] == num_riders)
    assert(results["unloaded"] == num_riders)
    num_benches_used = calculate_cycles_needed(num_riders, 10, 2)
    assert(results["num_benches"] == num_benches_used)


@pytest.mark.lift
@pytest.mark.long
@pytest.mark.parametrize("num_benches",[5,10,15,20])
def test_lift_long(long_line, num_benches):
    num_riders = len(long_line)
    lift = Lift(num_benches)
    results = lift.simulate(long_line)
    assert(results["loaded"] == num_riders)
    assert(results["unloaded"] == num_riders)
    num_benches_used = calculate_cycles_needed(num_riders, num_benches, 2)
    assert(results["num_benches"] == num_benches_used)


