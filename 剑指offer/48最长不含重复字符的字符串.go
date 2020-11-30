func lengthOfLongestSubstring_1(s string) int {
	// 方法一 滑动窗口
	left := 0
	right := left
	cnt := [256]int{}
	res := 0
	for right < len(s) {
		cnt[s[right]]++
		for cnt[s[right]] > 1 {
			if cnt[s[left]] > 0 {
				cnt[s[left]]--
				left++
			}
		}
		cur := right - left + 1
		if cur > res {
			res = cur
		}
		right++
	}
	return res
}

// 方法二 记录上一次某字符出现的位置
func lengthOfLongestSubstring(s string) int {
	lastApp := [256]int{}
	for i, _ := range lastApp {
		lastApp[i] = -1
	}
	res := 0
	left := 0
	for i, c := range s {
		if lastApp[c] >= left {
			left = lastApp[c] + 1
		} else if i-left+1 > res {
			res = i - left + 1
		}
		lastApp[c] = i
	}
	return res
}