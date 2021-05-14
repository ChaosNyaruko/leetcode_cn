class Solution:
    SYMBOLS = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
    ]
    def intToRoman(self, num: int) -> str:
        res = []
        for s, v in Solution.SYMBOLS:
            while num >= v:
                num -= v
                res.append(s)
            if num == 0:
                break

        return ''.join(res)
