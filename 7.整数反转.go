/*
 * @lc app=leetcode.cn id=7 lang=golang
 *
 * [7] 整数反转
 */

// @lc code=start
func reverse(x int) int {
	var result int
	var sign int
	if x > 0 {
		sign = 1
	} else {
		sign = -1
	}
	y := uint64(abs(int64(x)))
	for y != 0 {
		tail := int(y % 10)
		if result > int(MaxInt/10) || int(MaxInt)-tail < 10*result {
			return 0
		}
		tmpRes := 10*result + tail
		result = tmpRes
		y /= 10
	}
	return sign * result
}

// 1534236469

const MaxUint = ^uint32(0)
const MinUint = 0
const MaxInt = int32(MaxUint >> 1)
const MinInt = -MaxInt - 1

func abs(x int64) int64 {
	if x >= 0 {
		return x
	} else {
		return -x
	}
}

// @lc code=end

