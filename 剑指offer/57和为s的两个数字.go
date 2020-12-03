func twoSum(nums []int, target int) []int {
	l, r := 0, len(nums)-1
	for l < r {
		if nums[l]+nums[r] == target {
			return []int{nums[l], nums[r]}
		} else if nums[l]+nums[r] > target {
			r--
		} else {
			l++
		}
	}
	return []int{}
}