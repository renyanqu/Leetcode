### use two pointers method + sorted
def three_sum_two_pointers(nums: list) -> list:
    answer = []
    nums = sorted(nums)
    for i in range(len(nums)-2):
        if nums[i] > 0:
            break
        else:
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            seen = {}
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    if (nums[left], nums[right]) not in seen:
                        seen[(nums[left], nums[right])] = i
                        answer.append([nums[i], nums[left], nums[right]])
                        right -= 1
                        left += 1
                    else:
                        right -= 1
                        left += 1

    return answer


### use hashtable non sort fashion
def three_sum_hash(nums: list) -> list:
    solution = set()
    if len(nums) < 3:
        return solution
    elif len(nums) == 3:
        if nums[0] + nums[1] + nums[2] == 0:
            return nums
        else:
            return solution

    else:
        for i in range(len(nums)-2):
            seen = {}
            for j in range(i+1, len(nums)):
                if nums[j] not in seen:
                    seen[nums[j]] = j
                if -nums[i]-nums[j] in seen and seen[-nums[i]-nums[j]] != j:
                    solution.add(tuple(sorted((nums[i], nums[j], -nums[i]-nums[j]))))
        return list(solution)


print(three_sum_hash([-1,0,1,2,-1,-4]))



for i in [1,2,3]:
    print(i)
else:
    print("loop finished!")


##################################################
def three_sum2(nums: list) -> list:
    answer = []
    nums = sorted(nums)
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        else:
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1

    return set(answer)


print(three_sum([-2,0,0,2,2]))

print(three_sum2([-2,0,0,2,2]))