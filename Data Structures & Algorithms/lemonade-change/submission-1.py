class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billCount = dict()
        billCount[5] = 0
        billCount[10] = 0
        billCount[20] = 0
        for i in bills:
            if i == 5:
                billCount[5] += 1
            if i == 10:
                if billCount[5] > 0:
                    billCount[5] -= 1
                    billCount[10] += 1
                else:
                    return False
            if i == 20:
                if billCount[10] > 0 and billCount[5] > 0:
                    billCount[5] -= 1
                    billCount[10] -= 1
                    billCount[20] += 1
                elif billCount[5] > 2:
                    billCount[5] -= 3
                    billCount[20] += 1
                else:
                    return False

        return True


        