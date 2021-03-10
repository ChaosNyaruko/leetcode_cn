class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        res = 0
        i = 0
        ops = [1]
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < len(s) and (ord(s[i]) - ord('0')) >= 0 and (ord(s[i]) - ord('0')) <=9:
                    num =10 * num + (ord(s[i]) - ord('0'))
                    i += 1
                res += sign * num

        return res
