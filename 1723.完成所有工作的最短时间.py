class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def dfs(workload, idx, limit):
            if idx >= len(jobs):
                return True

            cur = jobs[idx]
            for i, v in enumerate(workload):
                if v + cur <= limit:
                    workload[i] += cur
                    if dfs(workload, idx + 1, limit):
                        return True
                    workload[i] -= cur

                if workload[i] == 0 or workload[i] + cur == limit:
                    break

            return False

        def check(limit):
            workload = [0] * k
            return dfs(workload, 0, limit)

        jobs.sort(reverse=True)
        l, r = jobs[0], sum(jobs)
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                r = m
            else:
                l = m + 1

        return l
