class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        anagramS = {}
        anagramT = {}

        for c in s:
            anagramS[c] = 1 if c not in anagramS else anagramS[c] + 1
        for c in t:
            anagramT[c] = 1 if c not in anagramT else anagramT[c] + 1
        
        # iterate through anagramS, if not in anagamT or values not equal return false
        # or can i just do
        return anagramS == anagramT

        