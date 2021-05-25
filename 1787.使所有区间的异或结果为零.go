import "math"

func minChanges(nums []int, k int) int {
	const inf = math.MaxInt32 / 2
	const maxX = 1 << 10
	n := len(nums)

	f := make([]int, maxX)
	for i := range f {
		f[i] = inf
	}
	f[0] = 0

	for i := 0; i < k; i++ {
		size := 0
		cnt := make(map[int]int)
		for j := i; j < n; j += k {
			cnt[nums[j]]++
			size++
		}
		t2Min := min(f...)

		g := make([]int, maxX)
		for j := range g {
			g[j] = t2Min
		}
		for mask := range g {
			for x, c := range cnt {
				g[mask] = min(g[mask], f[mask^x]-c)
			}
		}

		for j := range g {
			g[j] += size
		}

		f = g
	}
	return f[0]
}

func min(a ...int) int {
	res := a[0]
	for _, v := range a[1:] {
		if v < res {
			res = v
		}
	}
	return res
}
