class Solution:
    def checkRecord(self, s: str) -> bool:
        absents, lates = 0, 0
        for c in s:
            if c == 'A':
                absents += 1

            if c == 'L':
                lates += 1
            else:
                lates = 0

            if absents >= 2 or lates >= 3:
                return False

        return True
