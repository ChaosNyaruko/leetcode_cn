class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        next_ = first
        for e in encoded:
            next_ = next_ ^ e
            res.append(next_)

        return res

