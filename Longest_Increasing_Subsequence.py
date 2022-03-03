def lengthOfLIS(nums: list) -> int:
    sub = []
    for i in range(len(nums)):
        if len(sub) == 0:
            sub.append(nums[i])
        else:
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            if nums[i] < sub[-1]:
                if len(sub) == 1:
                    sub[-1] = nums[i]

                else:
                    if nums[i] > sub[-2]:
                        sub[-1] = nums[i]

    return sub

print(lengthOfLIS([8,1,6,2,3,10]))
for i in range(5):
    for j in range(i,5):
        print(i,j)