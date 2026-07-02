class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # add each value to set, if in set return false
        appeared = set()
        for num in nums:
            if num in appeared:
                return True
            appeared.add(num)
        return False
        