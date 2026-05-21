class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        # go through first time multiplying each value
        for i in range(1, len(nums)):
            output.append(output[i-1]*nums[i-1])

        # second time go backwards to get full procut execpt self 
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]
        return output
        