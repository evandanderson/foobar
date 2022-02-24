"""
You have L, a list containing some digits (0 to 9). Write a function solution(L)
which finds the largest number that can be made from some or all of these digits
and is divisible by 3. If it is not possible to make such a number, return 0 as
the solution. L will contain anywhere from 1 to 9 digits.  The same digit may
appear multiple times in the list, but each element in the list may only be used once.
"""

# ordered list of the greatest sum that is / by 3

# want to check if divisible by 3 and remove the least amount of digits as possible

# use the quotient to determine the next digit to be removed


def solution(l):
    ordered_list = sorted(l, reverse=True)
    list_sum = sum(ordered_list)
    while list_sum % 3 > 0:
        if len(ordered_list) > 1:
            for i in reversed(range(len(ordered_list))):
                if list_sum % 3 - ordered_list[i] % 3 == 0:
                    ordered_list.pop(i)
                    break
                elif i == 0:
                    ordered_list.pop(len(ordered_list) - 1)
            list_sum = sum(ordered_list)
        else:
            return 0
    return sum(num * 10**i for i, num in enumerate(ordered_list[::-1]))