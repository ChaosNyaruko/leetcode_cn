/*
 * @lc app=leetcode.cn id=75 lang=golang
 *
 * [75] 颜色分类
 */

// @lc code=start
func sortColors(nums []int) {
	zeros := -1
	twos := len(nums)
	for i := 0; i < twos; {
		if nums[i] == 0 {
			zeros++
			nums[zeros], nums[i] = nums[i], nums[zeros]
			i++
		} else if nums[i] == 1 {
			i++
		} else {
			twos--
			nums[twos], nums[i] = nums[i], nums[twos]
		}
	}
}

// @lc code=end

