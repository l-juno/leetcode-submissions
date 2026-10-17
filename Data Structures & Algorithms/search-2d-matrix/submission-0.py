class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][0] <= target and matrix[mid][len(matrix[0])-1] >= target:
                return self.hasTarget(matrix[mid], target)
            elif matrix[mid][0] < target:
                start = mid + 1
            else: 
                end = mid - 1
        return False

    def hasTarget(self, nums, target):
        start = 0 
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid + 1
            else: 
                end = mid - 1
        return False
            
        