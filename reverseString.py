s = "  Bob    Loves  Alice   "
len(s.strip(" ").split(" ")[1])
list(" ".join(s.strip().split()))


def reverseWords(s: str) -> None:
    sentence = "".join(s)
    words_array = sentence.split()
    left, right = 0, len(words_array) - 1
    print(words_array)
    while left < right:
        words_array[left], words_array[right] = words_array[right], words_array[left]
        left += 1
        right -= 1

    words_array = " ".join(words_array)
    print(words_array)
    return list(words_array)

print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))