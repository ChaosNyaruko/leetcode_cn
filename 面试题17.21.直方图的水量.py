class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stk = []
        for i, h in enumerate(height):
            while stk and height[stk[-1]] < h:
                top = stk.pop()
                htop = height[top]
                if stk:
                    res += (min(h, height[stk[-1]]) - htop) * (i - stk[-1] - 1)
            stk.append(i)
        return res
