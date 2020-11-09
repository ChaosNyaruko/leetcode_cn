/*
 * @lc app=leetcode.cn id=39 lang=golang
 *
 * [39] 组合总和
 */

// @lc code=start
func helper(start, curSum, target int, candidates []int, path *[]int, res *[][]int) {
	if curSum > target {
		return
	}
	if curSum == target {
		// fmt.Println(*path)
		// fmt.Printf("before append res:%#v\n", *res)
		pathCopy := make([]int, len(*path))
		copy(pathCopy, *path)
		*res = append(*res, pathCopy)
		// fmt.Println(*res)
		return
	}
	for i := start; i < len(candidates); i++ {
		*path = append(*path, candidates[i])
		helper(i, curSum+candidates[i], target, candidates, path, res)
		*path = (*path)[:len(*path)-1]
	}
	return
}
func combinationSum(candidates []int, target int) [][]int {
	path := make([]int, 0)
	res := make([][]int, 0)
	helper(0, 0, target, candidates, &path, &res)
	return res
}

// @lc code=end

