# Suppose we have very large sparse vectors (most of the elements in vector are zeros)

# Find a data structure to store them
# Compute the Dot Product.

def dot_product(arr1: list, arr2: list) -> int:
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]

    return sum


def dot_product2(dict1: dict, dict2: dict) -> int:
    sum = 0
    for k, v in dict1:
        if k in dict2:
            sum += dict1[k] * dict2[k]

    return sum


a = [1, 0, 0, 0, 0, 1, 2, 0, 10 ^ 15 0sss]
b = [1, 0, 0, 0, 0, 0, 3, 1, 10 ^ 15 0sss]
print(dot_product(a, b))

lookup = {}
for num in a:
    if num not in lookup:
        lookup[num] = 1

    else:
        lookup[num] += 1

a = {0: 1, 5: 1, 6: 2}
b = {0: 1, 6: 3}

