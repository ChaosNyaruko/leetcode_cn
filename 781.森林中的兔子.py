class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        return sum((n + x) // (x + 1) * (x + 1)for x, n in count.items())
