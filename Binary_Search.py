def Binary_Search(nums: list, target: int) -> bool:
    l, r = 0, len(nums) - 1
    while l <= r:
        middle = (l + r) // 2
        if nums[middle] > target:
            r = middle - 1
        elif nums[middle] < target:
            l = middle + 1
        else:
            return middle


    return -1

### variations 1
### find the first one that equal target
def Binary_Search1(nums: list, target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        middle = (l + r) // 2
        if l == r:
            return l
        if nums[middle] > target:
            r = middle - 1
        elif nums[middle] < target:
            l = middle + 1
        else:
            r = middle
    return -1

### find the last one that equals the target
def Binary_Search2(nums: list, target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if l == r:
            return l
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            l = mid

    return -1


### find the first values that is >= target
def Binary_Search3(nums: list, target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if l == r:
            return l
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    return -1


### find the last value that is <= target
def Binary_Search4(nums: list, target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if l == r:
            return l
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid
    return -1













print(Binary_Search([0,4,8,8,8,8,8,10],8))

print(Binary_Search1([1,2,8,8],8))
print(Binary_Search2([1,2,8,8],8))
print(Binary_Search3([1,2,3,4,5,8,8],8))
print(Binary_Search4([1,2,3,4,5,8,8],8))