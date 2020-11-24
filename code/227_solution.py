class Solution:
    def calculate(self, s: str) -> int:
        operators = set("+-*/")
        n = len(s)
        num, sign = 0, "+"
        stack = []
        for i, c in enumerate(s):
            if c.isdigit(): num = num * 10 + int(c)
            if c in operators or i == n - 1:
                if sign == "+": stack.append(num)
                elif sign == "-": stack.append(-num)
                elif sign == "*": stack.append(stack.pop() * num)
                else: stack.append(int(stack.pop() / num))
                num = 0
                sign = c
        return sum(stack)
