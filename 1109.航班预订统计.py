class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n

        for booking in bookings:
            l, r, inc = booking[0], booking[1], booking[2]
            res[l - 1] += inc
            if r < n:
                res[r] -= inc

        for i in range(1, len(res)):
            res[i] += res[i - 1]

        return res
