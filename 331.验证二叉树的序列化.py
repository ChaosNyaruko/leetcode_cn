class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        i = 0
        while i < len(preorder):
            if slots == 0:
                return False
            if preorder[i] == ',':
                i += 1
            elif preorder[i] == '#':
                slots -= 1
                i += 1
            else:
                while i < len(preorder) and preorder[i] != ',':
                    i += 1
                slots += 1
        return slots == 0
