class Solution:
    def checkValidString(self, s: str) -> bool:
        mx, mn = 0, 0
        for c in s:
            if c == '(':
                mx += 1
                mn += 1
            elif c == ')':
                mn = max(mn - 1, 0)
                mx -= 1
                if mx < 0:
                    return False
            elif c == '*':
                mn = max(mn - 1, 0)
                mx += 1

        return mn == 0
