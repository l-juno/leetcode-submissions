class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(num1, num2, op):
            if op == "+":
                return num1 + num2
            elif op == "-":
                return num2 - num1
            elif op == "*":
                return num1 * num2
            elif op == "/":
                return num2 / num1
        
        arr = []
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                arr.append(calculate(int(arr.pop()), int(arr.pop()), i))
            else:
                arr.append(i)
        return int(arr.pop())
        