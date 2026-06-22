class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        current = 0
        currSub = set()
        left = 0
        for i in range(len(s)):
            # check if in set
            if s[i] in currSub:
                while s[i] in currSub:
                    currSub.remove(s[left])
                    left += 1
            currSub.add(s[i])
            longest = max(longest, i - left + 1)
        return longest
