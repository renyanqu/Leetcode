import re
inp_str = "   Bob hit a ball, the hit BALL flew far after it was hit.   "
inp_str2 = "a, a, a, a, b,b,b,c, c"
inp_str = inp_str.strip()
opt = re.sub(r'[^\w\s]', '', inp_str2).lower()
opt_array = opt.split()
print(opt_array)

normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in inp_str2])

def mostCommonWord(paragraph:str, banned_str:list) -> str:
    clean_pgh = paragraph.strip()
    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in clean_pgh])
    word_array = normalized_str.split()
    word_count = {}
    for word in word_array:
        if word not in set(banned_str):
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1

    max_frequence = max(word_count.values())
    for key, value in word_count.items():
        if value == max_frequence:
            return key







print(mostCommonWord(inp_str,banned_str=["hit"]))
print(mostCommonWord(inp_str2,banned_str=[]))