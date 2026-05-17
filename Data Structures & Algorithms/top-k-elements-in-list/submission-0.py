class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # results list
        results = []

        # iterate array and go create count dictionary
        numsCount = dict()
        for num in nums:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
        
        # get highest count
        while k > 0:
            maxKey = max(numsCount, key=numsCount.get)
            print(maxKey)
            results.append(maxKey)
            numsCount[maxKey] = -1
            k -= 1
        
        return results

        