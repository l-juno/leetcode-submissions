class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        charSet = set(s)

        for c in charSet:
            currCount = 0
            start = 0
            for i in range(len(s)):
                if s[i] == c:
                    currCount += 1

                while (i - start + 1) - currCount > k:
                    if s[start] == c:
                        currCount -= 1
                    start += 1
                longest = max(longest, i-start+1)
        return longest
                
