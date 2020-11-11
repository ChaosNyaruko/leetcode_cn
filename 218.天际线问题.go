/*
 * @lc app=leetcode.cn id=218 lang=golang
 *
 * [218] 天际线问题
 */

// @lc code=start
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func helper(buildings [][]int, l, r int) [][]int {
	if l == r {
		return [][]int{{buildings[l][0], buildings[l][2]}, {buildings[l][1], 0}}
	}
	var res [][]int
	mid := l + (r-l)/2
	left := helper(buildings, l, mid)
	right := helper(buildings, mid+1, r)
	m := 0
	n := 0
	lpre := 0
	rpre := 0
	for m < len(left) || n < len(right) {
		if m >= len(left) {
			res = append(res, right[n])
			n++
		} else if n >= len(right) {
			res = append(res, left[m])
			m++
		} else { // 需要执行"merge"
			if left[m][0] > right[n][0] { // 使用right[n]
				if right[n][1] > lpre {
					res = append(res, right[n])
				} else if rpre > lpre {
					res = append(res, []int{right[n][0], lpre})
				}
				rpre = right[n][1]
				n++
			} else if left[m][0] < right[n][0] { // 使用left[m]
				if left[m][1] > rpre { //
					res = append(res, left[m])
				} else if lpre > rpre {
					res = append(res, []int{left[m][0], rpre})
				}
				lpre = left[m][1]
				m++
			} else {
				if left[m][1] >= right[n][1] && left[m][1] != max(lpre, rpre) {
					res = append(res, left[m])
				} else if left[m][1] <= right[n][1] && right[n][1] != max(lpre, rpre) {
					res = append(res, right[n])
				}
				lpre = left[m][1]
				rpre = right[n][1]
				m++
				n++
			}
		}
	}
	return res
}

func getSkyline(buildings [][]int) [][]int {
	if len(buildings) == 0 {
		return nil
	}
	return helper(buildings, 0, len(buildings)-1)
}

// @lc code=end

