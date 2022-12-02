import copy
from io import TextIOWrapper
import math


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    ratings = copy.deepcopy(lines)
    oxygen_generator_rating = []
    i = 0
    while len(ratings) > 1 and i < len(lines[0]):
        n = len(ratings)
        cols = [list(map(int, col)) for col in zip(*ratings)]
        modes = [1 if sum(col) >= n / 2 else 0 for col in cols]
        next_ratings = []
        for rating in ratings:
            if int(rating[0]) == modes[0]:
                next_ratings.append(rating[1:])
        oxygen_generator_rating.append(str(modes[0]))
        ratings = next_ratings
        i += 1
    oxygen_generator_rating.append(ratings[0])
    oxygen_generator_rating = ''.join(oxygen_generator_rating)
    oxygen_generator_rating = int(oxygen_generator_rating, 2)

    ratings = copy.deepcopy(lines)
    co2_scrubber_rating = []
    i = 0
    while len(ratings) > 1 and i < len(lines[0]):
        n = len(ratings)
        cols = [list(map(int, col)) for col in zip(*ratings)]
        modes = [0 if sum(col) >= n / 2 else 1 for col in cols]
        next_ratings = []
        for rating in ratings:
            if int(rating[0]) == modes[0]:
                next_ratings.append(rating[1:])
        co2_scrubber_rating.append(str(modes[0]))
        ratings = next_ratings
        i += 1
    co2_scrubber_rating.append(ratings[0])
    co2_scrubber_rating = ''.join(co2_scrubber_rating)
    co2_scrubber_rating = int(co2_scrubber_rating, 2)

    res = oxygen_generator_rating * co2_scrubber_rating

    # Finish your codes here
    return res
