class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def distance(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        st = distance([0, 0], target)
        for g in ghosts:
            gt = distance(g, target)
            if gt <= st:
                return False

        return True
