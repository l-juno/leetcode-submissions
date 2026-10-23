class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        uniqueSubstring = set()
        longest = 0
        currlen = 0
        for i in range(len(s)):
            if s[i] in uniqueSubstring:
                # pop until not in it and reset currLen to proper
                while s[i] in uniqueSubstring:
                    uniqueSubstring.remove(s[left])
                    left += 1
                currlen = i - left + 1
                uniqueSubstring.add(s[i])
            else:
                # add to set and + 1
                uniqueSubstring.add(s[i])
                currlen += 1
                longest = max(currlen, longest)
        return longest




        