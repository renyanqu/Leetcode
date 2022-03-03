def merge_sorted_list(l1: list, l2: list) -> list:
    merge_array = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merge_array.append(l1[i])
            i += 1
        else:
            merge_array.append(l2[j])
            j += 1

    if i == len(l1):
        return merge_array + l2[j:]
    if j == len(l2):
        return merge_array + l1[i:]


def merge_sort(arr: list):
    ### base case
    if len(arr) == 1:
        return arr
    ### recursive case
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_sorted_list(left, right)

merge_sort([5,4,3,2,1,4,4])