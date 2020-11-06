/*
 * @lc app=leetcode.cn id=20 lang=golang
 *
 * [20] 有效的括号
 */

// @lc code=start
var match = map[rune]rune{']': '[', '}': '{', ')': '('}

func isValid(s string) bool {
	stack := []rune{}
	for _, c := range s {
		if left, ok := match[c]; !ok {
			stack = append(stack, c)
		} else {
			if len(stack) == 0 || stack[len(stack)-1] != left {
				return false
			} else {
				// pop
				stack = stack[:len(stack)-1]
			}
		}
	}

	return len(stack) == 0
}

// @lc code=end

