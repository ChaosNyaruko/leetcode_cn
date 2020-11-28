func minArray(nums []int) int {
    l := 0
    r := len(nums) - 1
    for l < r && nums[l] >= nums[r] {
        m := l + (r - l) / 2
        if nums[l] > nums[m] {
            r = m
        } else if nums[m] > nums[r] {
			l = m + 1
		} else {
			l = l + 1
		}
	}
	return nums[l]
}