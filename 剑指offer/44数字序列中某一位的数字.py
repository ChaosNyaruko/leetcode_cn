class Solution:
    def findNthDigit(self, n: int) -> int:
        def countOfIntegers(digits):
            if digits == 1:
                return 10
            cnt = 10 ** (digits - 1)
            return 9 * cnt

        

        def helper(index, digits):
            begin = 1
            if digits == 1:
                begin = 0
            else:
                begin = 10 ** (digits - 1)
            
            number = begin + index / digits
            for i in range(0, digits - 1 - index % digits):
                number /= 10
            return number % 10

        if n < 0:
            return -1
        digits = 1
        while True:
            numbers = countOfIntegers(digits)
            if n < numbers * digits:
                return int(helper(n, digits))
            n -= digits * numbers
            digits += 1
        return -1

            