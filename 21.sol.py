import operator
from pathlib import Path
import re
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input21.txt")

OPMAP = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.floordiv
}

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()

    # first, let's get all the monkeys with known yell values
    yell_pattern = re.compile(r"([a-z]{4}): (\d+)")
    calc_pattern = re.compile(r"([a-z]{4}): ([a-z]{4}) (.){1,2} ([a-z]{4})")

    # Part 1    
    monkeys: dict[str, int] = {}  # monkey: value    
    rows_to_remove = []
    for row, line in enumerate(data):
        if match := yell_pattern.match(line):
            monkeys[match.groups()[0]] = int(match.groups()[1])
            rows_to_remove.append(row)

    # strip out the known monkeys, and leave only the calculations
    calcs_only = [line for row, line in enumerate(data) if row not in rows_to_remove]
    
    calcs = {} # Assemble a dict of {monkey_id: (monkey, op, monkey), ...}
    for line in calcs_only:
        monkey_id, monkey2, op, monkey3 = calc_pattern.findall(line)[0]
        calcs[monkey_id] = (monkey2, op, monkey3)

    evaluate_monkey("root", calcs, monkeys)
    print(f"Part 1: root={monkeys['root']}")
    
    # Part 2
    monkeys = {}  # recreate known monkeys, {monkey: value}
    for row, line in enumerate(data):
        if match := yell_pattern.match(line):
            monkeys[match.groups()[0]] = int(match.groups()[1])

    # change the root monkey instruction. We'll change it to a subtract operator.
    # That way, we'll know both operands have the same value when the result is 0
    calcs["root"] = (calcs["root"][0], "-", calcs["root"][2])
    
    # We need to try values that will sresult in root == 0.
    # Brute force is really slow, but binary search works well!
    humn = binary_search(0, 0, 1e16, try_monkeys, calcs, monkeys)
    if humn is None: # try reverse correlation binary search
        humn = binary_search(0, 0, 1e16, try_monkeys, calcs, monkeys, reverse_search=True)
    print(f"Part 2: humn={humn}")
    
def binary_search(target, low:int, high:int, func, *func_args, reverse_search=False) -> int:
    """ Generic binary search function that takes a target to find,
    low and high values to start with, and a function to run, plus its args. 
    Implicitly returns None if the search is exceeded. """
    
    res = None  # just set it to something that isn't the target
    candidate = 0  # initialise; we'll set it to the mid point in a second
    
    while low < high:  # search exceeded        
        candidate = int((low+high) // 2)  # pick mid-point of our low and high        
        res = func(candidate, *func_args) # run our function, whatever it is
        if res == target:
            return candidate  # solution found
        comp = operator.gt if not reverse_search else operator.lt
        if comp(res, target):
            low = candidate
        else:
            high = candidate

def try_monkeys(candidate, calcs: dict, monkeys: dict) -> int:
    monkeys_try = monkeys.copy()
    monkeys_try["humn"] = candidate
    res = evaluate_monkey("root", calcs, monkeys_try)
    return res
    
def evaluate_monkey(monkey_id: str, calcs, monkeys) -> int:
    """ Recursive evaluation of calcs like: pppw + sjmn """
    current_calc = calcs[monkey_id]
    monkey2, monkey3 = current_calc[0], current_calc[2]
    op = current_calc[1]
    
    # recurse for monkeys we don't yet know value for
    if monkey2 not in monkeys:
        evaluate_monkey(monkey2, calcs, monkeys)
    if monkey3 not in monkeys:
        evaluate_monkey(monkey3, calcs, monkeys)

    # base case
    # We could use eval, but it's dangerous, and relatively slow
    # monkeys[monkey_id] = int(eval(str(monkeys[monkey2]) + op + str(monkeys[monkey3])))
    monkeys[monkey_id] = OPMAP[op](monkeys[monkey2], monkeys[monkey3])
    
    return monkeys[monkey_id]
            
if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")