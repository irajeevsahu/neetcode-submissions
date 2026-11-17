class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ["+", "-", "*", "/"]:
                a = stack.pop()
                b = stack.pop()
                if c == "+":
                    ans = b + a
                elif c == "-":
                    ans = b - a
                elif c == "*":
                    ans = b * a
                elif c == "/":
                    ans = int(float(b) / a)
                stack.append(ans)
            else:
                stack.append(int(c))
        return stack.pop()
