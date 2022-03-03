def longestPalindrome(s:str) -> str:
    dp_arrays = [[0 for i in range(len(s))] for j in range(len(s))]
    if len(s) == 1:
        return s
    ### length == 1,2 substring
    i = 0
    while i < len(s):
        dp_arrays[i][i] = 1
        i += 1

    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            dp_arrays[i][i+1] = 1
        i += 1


    ### length > 2
    if len(s) > 2:
        for k in range(3, len(s)+1):
            l = 0
            #r = k + l - 1
            while l < len(s) + 1 - k:
                if s[l] == s[k + l - 1]:
                    dp_arrays[l][k + l - 1] = dp_arrays[l+1][k + l - 2]
                l += 1


    max_len = 1
    answer = ''
    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp_arrays[i][j] == 1 and max_len < j - i + 1:
                max_len = j - i + 1
                answer = s[i:j+1]

    return answer

print(longestPalindrome("abcba"))
