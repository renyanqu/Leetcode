import sys


def minWindow(s: str, t: str) -> str:
    left, right = 0, 0
    answer, min_size = '', sys.maxsize
    while left <= right and right < len(s):
        if verify(s[left:right + 1], t):
            if min_size > (right + 1 - left):
                min_size = right + 1 - left
                answer = s[left:right + 1]
            left += 1

        else:
            right += 1

    return answer


def verify(substring, target):
    lookup1, lookup2 = {}, {}
    for char in substring:
        if char not in lookup1:
            lookup1[char] = 1
        else:
            lookup1[char] += 1

    for char in target:
        if char not in lookup2:
            lookup2[char] = 1
        else:
            lookup2[char] += 1

    for key, value in lookup2.items():
        if key not in lookup1:
            return False
        else:
            if lookup2[key] > lookup1[key]:
                return False
    return True

s = "ACA"
t = "AA"


print(minWindow(s,t))
