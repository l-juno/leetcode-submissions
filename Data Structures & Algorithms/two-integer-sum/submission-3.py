class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in targetDict:
                return [targetDict[difference], i]
            else:
                targetDict[nums[i]] = i
        return [0, 0]
            