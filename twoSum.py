### brutal force space O(1), time O(N^2)

def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if num[i] + nums[j] == target:
                return [i, j]


### use sorted first and then two pointers O(NlogN) + O(N)

def twoSum2(nums: list, target: int) -> list:
    sorted_nums = sorted(nums)
    p1, p2 = 0, len(nums) - 1
    val1, val2 = 0, 0
    while p1 < p2:
        if sorted_nums[p1] + sorted_nums[p2] > target:
            p2 -= 1
        elif sorted_nums[p1] + sorted_nums[p2] < target:
            p1 += 1
        else:
            val1, val2 = sorted_nums[p1], sorted_nums[p2]
            break
    output = []
    for i in range(len(nums)):
        if nums[i] == val1 or nums[i] == val2:
            output.append(i)

    return output



###  use hashmap store value, index pairs

def twoSum3(self, nums: list, target: int) -> list:
    lookup = {}
    for i in range(len(nums)):
        if nums[i] not in lookup:
            lookup[nums[i]] = i

        if target - nums[i] in lookup and i != lookup[target - nums[i]]:
            return [i, lookup[target - nums[i]]]


def two_sum(nums: list, target: int) -> list:
    answer = []
    seen = {}
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[nums[i]] = i

        if target-nums[i] in seen and i != seen[target-nums[i]]:
            answer.append([i, seen[target-nums[i]]])

    return answer


print(two_sum([1,2,3,4,5,6],7))











