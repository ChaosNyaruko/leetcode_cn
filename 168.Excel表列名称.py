class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 1 A   26 Z 27 AA 28 AB
        s = ""
        while columnNumber:
            s += chr((columnNumber - 1)%26 + ord('A'))
            columnNumber = (columnNumber - 1) // 26
        return s[::-1]
