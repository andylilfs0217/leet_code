"""
Dodge the Lasers!
=================

Oh no! You've managed to escape Commander Lambda's collapsing space station in an escape pod with the rescued bunny workers - but Commander Lambda isnt about to let you get away that easily. Lambda sent an elite fighter pilot squadron after you -- and they've opened fire!

Fortunately, you know something important about the ships trying to shoot you down. Back when you were still Lambda's assistant, the Commander asked you to help program the aiming mechanisms for the starfighters. They undergo rigorous testing procedures, but you were still able to slip in a subtle bug. The software works as a time step simulation: if it is tracking a target that is accelerating away at 45 degrees, the software will consider the targets acceleration to be equal to the square root of 2, adding the calculated result to the targets end velocity at each timestep. However, thanks to your bug, instead of storing the result with proper precision, it will be truncated to an integer before adding the new velocity to your current position.  This means that instead of having your correct position, the targeting software will erringly report your position as sum(i=1..n, floor(i*sqrt(2))) - not far enough off to fail Commander Lambdas testing, but enough that it might just save your life.

If you can quickly calculate the target of the starfighters' laser beams to know how far off they'll be, you can trick them into shooting an asteroid, releasing dust, and concealing the rest of your escape.  Write a function solution(str_n) which, given the string representation of an integer n, returns the sum of (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range 1 to n, it adds up all of the integer portions of i*sqrt(2).

For example, if str_n was "5", the solution would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in front of you, but on what you don't.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution('77')
Output:
    4208

Input:
Solution.solution('5')
Output:
    19

-- Python cases --
Input:
solution.solution('77')
Output:
    4208

Input:
solution.solution('5')
Output:
    19

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
"""

from decimal import Decimal, localcontext
from math import floor


def solution(s):
    with localcontext() as ctx:
        ctx.prec = 102
        n = Decimal(s)
        r = Decimal(2).sqrt()
        s = Decimal(2) + r

        def helper(n):
            if n < 1:
                return 0
            bnr = int(n * r)
            new_n = int(Decimal(bnr) / s)
            ans = bnr * (bnr + 1) / 2 - helper(new_n) - new_n * (new_n + 1)
            return ans

        ans = int(helper(n))
        return str(ans)


print(
    solution(
        '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
    ) ==
    '70710678118654752440084436210484903928483593768847403658833986899536623923105351942519376716382078638821760123411090095254685423841027253480565451739737157454059823250037671948325191776995310741236436'
)
print(solution('1000000') == '707106988293')
print(solution('999999') == '707105574080')
print(solution('99999') == '7070947101')
print(solution('9999') == '70698607')
print(solution('999') == '705900')
print(solution('99') == '6951')
print(solution('9') == '59')
print(solution('77') == '4208')
print(solution('5') == '19')
