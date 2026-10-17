class Solution:
    def isValid(self, s: str) -> bool:
        closingBracket = dict()
        closingBracket["}"] = "{"
        closingBracket["]"] = "["
        closingBracket[")"] = "("
        brackets = []
        for c in s:
            if c in closingBracket:
                if len(brackets) == 0:
                    return False
                openingBracket = brackets[-1]
                if openingBracket != closingBracket[c]:
                    return False
                else:
                    brackets.pop()
            else:
                brackets.append(c)
        return True if len(brackets) == 0 else False


        