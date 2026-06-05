class Solution:
    def isValid(self, s: str) -> bool:
        parentheseDict = dict()
        parentheseDict["]"] = "["
        parentheseDict[")"] = "("
        parentheseDict["}"] = "{"

        stack = []
        for c in s:
            if c in parentheseDict:
                if stack and parentheseDict[c] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True 
        else:
            return False