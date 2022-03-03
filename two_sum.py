def two_sum(nums: list, target):
    ans = (0, None, None)
    lookup = {}
    for i in range(len(nums)):
        if target - nums[i] in lookup and i != lookup[target - nums[i]]:
            if ans[0] < i - lookup[target - nums[i]]:
                ans = (i - lookup[target - nums[i]] + 1, lookup[target - nums[i]], i)
        if nums[i] not in lookup:
            lookup[nums[i]] = i

    return nums[ans[1]], nums[ans[2]], ans[0]

print(two_sum([1,1,0], 1))
