class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set, if in set return true
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            numSet.add(num)
        return False
        