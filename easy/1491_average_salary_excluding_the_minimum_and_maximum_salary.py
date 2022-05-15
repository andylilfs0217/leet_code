from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        max_salary, min_salary = salary[0], salary[0]
        for sal in salary:
            sum += sal
            max_salary = max(max_salary, sal)
            min_salary = min(min_salary, sal)
        return (sum-max_salary-min_salary)/(len(salary)-2)
