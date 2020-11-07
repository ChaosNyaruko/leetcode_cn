/*
 * @lc app=leetcode.cn id=31 lang=golang
 *
 * [31] 下一个排列
 *
 * https://leetcode-cn.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (34.62%)
 * Likes:    724
 * Dislikes: 0
 * Total Accepted:    97.2K
 * Total Submissions: 280.9K
 * Testcase Example:  '[1,2,3]'
 *
 * 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
 * 
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 * 
 * 必须原地修改，只允许使用额外常数空间。
 * 
 * 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 * 
 */

// @lc code=start
func reverse(nums []int) {
	l := 0
	r := len(nums) - 1
	for l < r {
		nums[l], nums[r] = nums[r], nums[l]
		l++
		r--
	}
	return
}

func nextPermutation(nums []int)  {
	n := len(nums)
	k := n - 2
	for ; k >= 0; k-- {
		if nums[k] < nums[k+1] {
			break
		}
	}
	if k < 0 {
		reverse(nums)
		return
	}
	// e.g. 1 2 3 4 5 8 7 6 
	// e.g. 1 2 3 4 6 8 7 5 -> 1 2 3 4 7 5 6 8 
	// nums[k]=5 nums[k+1]=8 根据k的计算条件，后面的序列一定是非增的
	// 需要找到8之后的最小的大于nums[k]的数
	l := n - 1
	for ;l > k; l-- {
		if nums[l] > nums[k] {
			break
		}
	}
	nums[k], nums[l] = nums[l], nums[k]
	reverse(nums[k+1:])
}
// @lc code=end

