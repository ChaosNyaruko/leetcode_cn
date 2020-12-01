func search(nums []int, target int) int {
	if len(nums) == 0 {
		return 0
	}
	l := 0
	r := len(nums) - 1
	// 找第一次出现的位置
	for l < r {
		m := l + (r-l)/2
		if nums[m] < target {
			l = m + 1
		} else {
			r = m
		}
	}
	if nums[l] != target {
		return 0
	}
	left := l
	// 找最后一次出现的位置
	l, r = 0, len(nums)-1
	for l < r {
		m := l + (r-l+1)/2
		if nums[m] > target {
			r = m - 1
		} else {
			l = m
		}
	}
	right := r
	return right - left + 1
}