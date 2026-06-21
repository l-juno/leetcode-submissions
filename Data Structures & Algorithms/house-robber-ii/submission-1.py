class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])


        def robber1(numsList):
            memo = [0] * len(numsList)
            memo[0] = numsList[0]
            memo[1] = max(numsList[0], numsList[1])
            for i in range(2, len(numsList)):
                memo[i] = max(memo[i-1], memo[i-2] + numsList[i])
            return max(memo[-1], memo[-2])

        return max(robber1(nums[1:]), robber1(nums[:n-1]))
        