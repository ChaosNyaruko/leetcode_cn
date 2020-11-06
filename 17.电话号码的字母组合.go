/*
 * @lc app=leetcode.cn id=17 lang=golang
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
var number2letters = [10]string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}
	res := make([]string, 0)
	p := &res // 为了防止在递归过程中slice发生重新内存分配导致值错误，res使用指针进行传递
	helper(0, digits, "", p)
	return *p
}

func helper(curInDigit int, digits string, path string, res *[]string) {
	if curInDigit == len(digits) {
		*res = append(*res, path)
		return
	}
	searchingSpace := number2letters[digits[curInDigit]-'0']
	for i := 0; i < len(searchingSpace); i++ {
		helper(curInDigit+1, digits, path+string(searchingSpace[i]), res)
		// 返回后path保持原状，无需手动回退
	}
	return
}

// @lc code=end

