### brutal force space O(1), time O(N^3)   loop through to list all substrings, scan the substrings to see if it
### has repeated characters, store its length if it doesn't have repeated characters and return max of all




def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 1 or len(s) == 0:
        return len(s)
    max = 1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            seen = {}
            # print(s[i:j+1])
            for ele in s[i:j + 1]:
                if ele not in seen:
                    seen[ele] = 1
                else:
                    seen[ele] += 1
            if len(seen.keys()) == len(s[i:j + 1]):
                if len(seen.keys()) > max:
                    max = len(seen.keys())

    return max
# two pointers sliding window
def longest_substring(s: str) -> int:
    if len(s) == 1 or len(s) == 0:
        return len(s)
    max_len = 1
    left, right = 0, 1
    while right < len(s):
        if check_duplicate(s[left:right+1]): #or left == right:
            if len(s[left:right+1]) > max_len:
                max_len = len(s[left:right+1])
            right += 1
        else:
            left += 1
            right += 1

    return max_len




def check_duplicate(s: str) -> bool:
    seen = {}
    for cha in s:
        if cha not in seen:
            seen[cha] = 1
        else:
            seen[cha] += 1
    if len(seen.keys()) < len(s):
        return False
    return True

print(longest_substring("bwf"))


print(lengthOfLongestSubstring("a"))


def len_longest_substring(s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)
    left, right, max_len = 0, 0, 0
    char_array = [0] * 128
    while right < len(s):
        r = s[right]
        char_array[ord(r)] += 1
        right += 1

        while char_array[ord(r)] > 1:
            l = s[left]
            char_array[ord(l)] -= 1
            left += 1

        max_len = max(max_len, right - left)

    return max_len


def len_longest_substring2(s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)
    left, right, max_len = 0, 0, 0
    char = {}
    while right < len(s):
        r = s[right]
        if r not in char:
            char[r] = 1
        else:
            char[r] += 1
        right += 1

        while char[r] > 1:
            l = s[left]
            char[l] -= 1
            left += 1

        max_len = max(max_len, right - left)

    return max_len


def len_longest_substring3(s: str) -> int:
    if len(s) == 0 or len(s) == 1:
        return len(s)
    left, right, max_len = 0, 0, 0
    char_count = {}
    char_index = {}
    while right < len(s):
        r = s[right]
        char_count[r] = 1 if r not in char_count else (char_count[r] + 1)
        char_index[r] = right if r not in char_index else
        while char_count[r] > 1:
            index = char_index[r]
            char_count[]




print(len_longest_substring2("abcabcbb"))
print(len_longest_substring2("bbbbb"))
print(len_longest_substring2("pwwkew"))





################### maximum water container


def max_water_container(height: list) -> int:
    max_water = 0
    for i in range(len(height)-1):
        for j in range(i+1,len(height)):
            water_contained = (j - i) * min(height[i],height[j])
            max_water = max(max_water,water_contained)

    return max_water


max_water_container([1,8,6,2,5,4,8,3,7])
max_water_container([1,1])
max_water_container([4,3,2,1,4])
max_water_container([1,2,1])