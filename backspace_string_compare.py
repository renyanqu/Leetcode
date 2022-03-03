class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1, r2 = len(s) - 1, len(t) - 1
        skip1, skip2 = 0, 0
        while r1 >= 0 or r2 >= 0:
            while r1 >= 0:
                if s[r1] == '#':
                    skip1 += 1
                    r1 -= 1
                elif skip1 > 0:
                    r1 -= 1
                    skip1 -= 1
                else:
                    break

            while r2 >= 0:
                if t[r2] == '#':
                    skip2 += 1
                    r2 -= 1
                elif skip2 > 0:
                    skip2 -= 1
                    r2 -= 1
                else:
                    break

            if r1 < 0 and r2 >= 0:
                return False
            if r2 < 0 and r1 >= 0:
                return False

            if s[r1] != t[r2]:
                return False

            r1 -= 1
            r2 -= 1

        return True



