import collections
import os
from y2022.q05.p2 import Solution


def Verify() -> collections.defaultdict:
    module_path = Solution.__file__
    module_dir = os.path.dirname(module_path)
    input_dir = module_dir + '/input/'
    solutions = collections.defaultdict()
    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'r') as f:
            solution = Solution.Solution(f)
            solutions[filename] = solution
    return solutions


def Output() -> None:
    solutions = Verify()
    for k, v in sorted(solutions.items()):
        print(f'{k}: {v}')


if __name__ == '__main__':
    Output()