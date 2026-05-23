class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create set for O(1) lookup
        numset = set(nums)
        longest = 0
        for num in nums:
            # not start
            if num-1 in numset:
                continue
            # start of sequence
            else:
                currLen = 0
                currNum = num
                while currNum in numset:
                    currLen += 1
                    currNum += 1
                longest = max(longest, currLen)
        return longest
                    
        