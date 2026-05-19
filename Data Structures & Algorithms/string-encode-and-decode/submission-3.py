class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0

        while i < len(s):
            # scan till you find #
            j = i
            while s[j] != '#':
                j += 1
            # keep the number and cast to int
            length = int(s[i:j])

            # front of string
            i = j + 1
            j = i + length
            res.append(s[i:j])

            # i is now at new length of next string
            i = j

        return res