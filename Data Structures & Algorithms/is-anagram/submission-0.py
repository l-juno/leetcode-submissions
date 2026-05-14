class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create dictionary of alphabets compare and return
        
        dictS = dict()
        dictT = dict()

        for letter in s:
            if letter in dictS:
                dictS[letter] += 1
            else:
                dictS[letter] = 1
        
        for letter in t:
            if letter in dictT:
                dictT[letter] += 1
            else:
                dictT[letter] = 1
        
        return dictS == dictT

        