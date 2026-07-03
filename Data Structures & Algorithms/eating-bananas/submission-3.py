class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l = 1
        res = maxPile
        while l <= maxPile:
            middleRate = (l + maxPile) // 2
            currHours = 0
            for pile in piles:
                currHours += math.ceil(pile / middleRate)

            if currHours <= h:
                res = min(res, middleRate)
                maxPile = middleRate - 1
            else: 
                l = middleRate + 1
        return res


        