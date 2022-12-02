from enum import Enum
from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    # res = Solution1(f)
    res = Solution2(f)
    return res


# Part 1
def Solution1(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    class Choice(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    WINS = set([
        (Choice.ROCK, Choice.SCISSORS),
        (Choice.SCISSORS, Choice.PAPER),
        (Choice.PAPER, Choice.ROCK),
    ])  # choice_left beats choice_right

    def getMatchPoint(o_choice: Choice, m_choice: Choice):
        points = 0
        result = (m_choice, o_choice)
        if o_choice == m_choice:
            # Draw: 3 points from draw + points from choice
            points += 3 + m_choice.value
        elif result in WINS:
            points += 6 + m_choice.value
        else:
            points += 0 + m_choice.value
        return points

    O_CONVERT = {'A': Choice.ROCK, 'B': Choice.PAPER, 'C': Choice.SCISSORS}
    M_CONVERT = {'X': Choice.ROCK, 'Y': Choice.PAPER, 'Z': Choice.SCISSORS}
    res = 0
    for line in lines:
        o_choice_str, m_choice_str = line.split(' ')
        o_choice, m_choice = O_CONVERT[o_choice_str], M_CONVERT[m_choice_str]
        points = getMatchPoint(o_choice, m_choice)
        res += points

    # Finish your codes here
    return res


# Part 1
def Solution2(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    class Choice(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    WINS = {
        Choice.ROCK: Choice.SCISSORS,
        Choice.SCISSORS: Choice.PAPER,
        Choice.PAPER: Choice.ROCK,
    }  # choice_key beats choice_value

    LOSES = {
        Choice.SCISSORS: Choice.ROCK,
        Choice.PAPER: Choice.SCISSORS,
        Choice.ROCK: Choice.PAPER,
    }  # choice_key beats choice_value

    def getMatchPoint(o_choice: Choice, m_choice: Choice):
        points = 0
        if o_choice == m_choice:
            # Draw: 3 points from draw + points from choice
            points += 3 + m_choice.value
        elif WINS[m_choice] == o_choice:
            points += 6 + m_choice.value
        else:
            points += 0 + m_choice.value
        return points

    def getMChoice(o_choice: Choice, m_result: int) -> Choice:
        if m_result == 3:
            m_choice = o_choice
        elif m_result == 0:
            m_choice = WINS[o_choice]
        else:
            m_choice = LOSES[o_choice]
        return m_choice

    O_CONVERT = {'A': Choice.ROCK, 'B': Choice.PAPER, 'C': Choice.SCISSORS}
    M_CONVERT = {'X': 0, 'Y': 3, 'Z': 6}
    res = 0
    for line in lines:
        o_choice_str, m_choice_str = line.split(' ')
        o_choice, m_result = O_CONVERT[o_choice_str], M_CONVERT[m_choice_str]
        m_choice = getMChoice(o_choice, m_result)
        points = getMatchPoint(o_choice, m_choice)
        res += points

    # Finish your codes here
    return res
