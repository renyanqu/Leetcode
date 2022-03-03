class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        l, r = 0, 0
        target = {}
        for char in t:
            if char not in target:
                target[char] = 1
            else:
                target[char] += 1

        while r < m:
            if self.verify(s[:r + 1], target):
                break
            else:
                r += 1

        ans = s[:r + 1]
        min_len = r - l + 1
        print(ans, min_len, l, r)
        while l <= r and r < m:
            while self.verify(s[l:r + 1], target):
                l += 1
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r + 1]
                print(l, r)
            while not self.verify(s[l:r + 1], target):
                r += 1
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans = s[l:r + 1]
                print(l, r)
        return ans

    def verify(self, substr: str, target: dict) -> bool:
        counter = {}
        for char in substr:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1

        for key, value in target.items():
            if key not in counter:
                return False
            else:
                if value > counter[key]:
                    return False
        return True

a, b = "ABAACBAB", "ABC"
solution = Solution()
print(solution.minWindow(a, b))