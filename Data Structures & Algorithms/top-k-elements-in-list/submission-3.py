class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        # create dictionary
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # create array for keys have value as index
        for key, v in count.items():
            freq[v].append(key)
        
        # create result array
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
    


        