/*
 * @lc app=leetcode.cn id=55 lang=golang
 *
 * [55] 跳跃游戏
 *
 * https://leetcode-cn.com/problems/jump-game/description/
 *
 * algorithms
 * Medium (41.36%)
 * Likes:    933
 * Dislikes: 0
 * Total Accepted:    171.3K
 * Total Submissions: 414.3K
 * Testcase Example:  '[2,3,1,1,4]'
 *
 * 给定一个非负整数数组，你最初位于数组的第一个位置。
 * 
 * 数组中的每个元素代表你在该位置可以跳跃的最大长度。
 * 
 * 判断你是否能够到达最后一个位置。
 * 
 * 示例 1:
 * 
 * 输入: [2,3,1,1,4]
 * 输出: true
 * 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
 * 
 * 
 * 示例 2:
 * 
 * 输入: [3,2,1,0,4]
 * 输出: false
 * 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
 * 
 * 
 */

// @lc code=start
func max(a,b int) int{
	if a > b {
		return a
	}
	return b
}

func canJump(nums []int) bool {
	if len(nums) == 0 {
		return false
	}
	furthest := 0
	for i := 0; i < len(nums) ; i++ {
		//fmt.Println("furthest:", furthest, "i+nums[i]", i + nums[i])
		if i <= furthest {
		furthest = max(furthest, i + nums[i])
			if furthest >= len(nums)-1 {
				return true
			} 
		}
	} 
	return false
}
// @lc code=end

