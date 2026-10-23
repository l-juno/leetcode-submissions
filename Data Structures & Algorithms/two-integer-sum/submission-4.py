class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [1, 2, 3, 4, 6, 8]
        # 11
        prevNum = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in prevNum:
                return [prevNum[difference], i]
            else:
                prevNum[nums[i]] = i
        
        return [-1, -1]
        