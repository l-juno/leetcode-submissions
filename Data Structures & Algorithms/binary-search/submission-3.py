class Solution:
    def search(self, nums: List[int], target: int) -> int:
        front = 0
        end = len(nums)
        while front < end:
            middle = (front + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                front = middle +1
            else:
                end = middle 

        return -1
        