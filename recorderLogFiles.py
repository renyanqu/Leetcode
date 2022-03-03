logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
#_id, rest = logs[1].split(" ", maxsplit=1)

def recorderLogsFile(logs:list) -> list:
    letter_array, digit_array = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digit_array.append(log)
        else:
            letter_array.append(log)
    sorted_letter = sorted(letter_array, key=sort_key)

    return sorted_letter + digit_array

def sort_key(log:str) -> tuple:
    identifier, rest = log.split(" ", maxsplit=1)
    return (rest, identifier)

print(recorderLogsFile(logs))