class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        end = len(s) - 1
        while front < end:
            print("front: " + s[front] + " end: " + s[end])
            if self.isNotAlphanumeric(s[front]):
                front += 1
                print("skip front")
                continue
            if self.isNotAlphanumeric(s[end]):
                end -= 1
                print("skip end")
                continue
            if s[front].lower() != s[end].lower():
                return False
            front += 1
            end -= 1
        return True

    def isNotAlphanumeric(self, c):
        return not c.isalnum()
            

        