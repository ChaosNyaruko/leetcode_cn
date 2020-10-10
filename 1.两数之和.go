/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	record := make(map[int]int)
	for i, num := range nums {
		c := target - num
		if idx, ok := record[c]; ok {
			return []int{i, idx}
		}
		record[num] = i
	}
	return []int{}
}

// @lc code=end

