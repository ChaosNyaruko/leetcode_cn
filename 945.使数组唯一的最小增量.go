func minIncrementForUnique(nums []int) int {
	cnt := make(map[int]int)
	for _, num := range nums {
		cnt[num]++
	}
	res := 0
	need := 0
	for i := 0; i < 80000; i++ {
		n, c := i, cnt[i]
		if c >= 2 {
			need += c - 1
			res -= n * (c - 1)
		} else if c == 0 && need > 0 {
			need--
			res += n
		}
		// c = 1 just continue
	}
	return res
}
