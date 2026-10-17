class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dfs(currIdx):
            if currIdx >= len(nums):
                result.append(subset.copy())
                return


            subset.append(nums[currIdx])
            dfs(currIdx+1)

            subset.pop()
            dfs(currIdx+1)

        dfs(0)

        return result
            
        


        