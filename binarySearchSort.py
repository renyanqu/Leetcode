### given a sorted array, sort it by binary search method, o(N) time and o(1) space
def binary_search_sort(arr: list, target: int, left: int, right: int) -> int:
    ### base case 1, no target found
    if left > right:
        return -1
    mid = (left + right) // 2

    ### base case 2, target found
    if arr[mid] == target:
        return mid
    ### recursive cases
    if arr[mid] > target:
        return binary_search_sort(arr, target, left, mid-1)
    if arr[mid] < target:
        return binary_search_sort(arr, target, mid+1, right)


binary_search_sort([1,2,3,4,5,6,7],40,0,6)