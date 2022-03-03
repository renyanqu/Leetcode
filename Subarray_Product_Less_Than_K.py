import math


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        log_prefix_sum = [0]
        total = 0
        ans = 0
        k = math.log(k)
        for num in nums:
            total += math.log(num)
            log_prefix_sum.append(total)

        for i in range(len(log_prefix_sum) - 1):
            for j in range(i + 1, len(log_prefix_sum)):
                if log_prefix_sum[j] - log_prefix_sum[i] < k:
                    ans += 1

        return ans