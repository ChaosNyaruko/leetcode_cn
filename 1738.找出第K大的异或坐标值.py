class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre = [[0 for _ in range(n + 1)] for _ in range(m+1)]
        res = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                pre[i][j] = pre[i-1][j] ^ pre[i][j-1] ^ pre[i-1][j-1] ^ matrix[i-1][j-1]
                res.append(pre[i][j])


        def nth_element(left, right, arr):
            if left == right:
                return

            pivot = random.randint(left, right)
            arr[pivot], arr[left] = arr[left], arr[pivot]

            pivot = arr[left]
            l, r = left + 1, right
            while l <= r:
                while l < right  and arr[l] >= pivot:
                    l += 1
                while r > left  and arr[r] <= pivot:
                    r -= 1
                if l >= r:
                    break
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

            arr[left], arr[r] = arr[r], arr[left]
            return r

        res.sort(reverse=True)
        return res[k - 1]
        #print(res)
        l, r = 0, len(res) - 1
        while l < r:
            p = nth_element(l, r, res)
            if p == k - 1:
                return res[p]
            elif p > k - 1:
                r = p - 1
            else:
                l = p + 1

        # print("out", l, k - 1)
        return res[k - 1]
