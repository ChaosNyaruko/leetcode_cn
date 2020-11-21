/*
 * @lc app=leetcode.cn id=49 lang=golang
 *
 * [49] 字母异位词分组
 *
 * https://leetcode-cn.com/problems/group-anagrams/description/
 *
 * algorithms
 * Medium (63.93%)
 * Likes:    523
 * Dislikes: 0
 * Total Accepted:    120.5K
 * Total Submissions: 188.4K
 * Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
 *
 * 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
 * 
 * 示例:
 * 
 * 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
 * 输出:
 * [
 * ⁠ ["ate","eat","tea"],
 * ⁠ ["nat","tan"],
 * ⁠ ["bat"]
 * ]
 * 
 * 说明：
 * 
 * 
 * 所有输入均为小写字母。
 * 不考虑答案输出的顺序。
 * 
 * 
 */

// @lc code=start
type sortRunes []rune

func (s sortRunes) Less(i, j int) bool {
    return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}

func (s sortRunes) Len() int {
    return len(s)
}

func SortString(s string) string {
    r := []rune(s)
    sort.Sort(sortRunes(r))
    return string(r)
}

func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string)
	for _, str := range strs {
		standard := SortString(str)
		tmp := append(m[standard], str)
		m[standard] = tmp 
	}
	res := make([][]string, len(m))
	i := 0
	for _, v := range m {
		if res[i] == nil {
			res[i] = make([]string, 0, 10)
		}
		for _, s := range v {
			res[i] = append(res[i], s)	
		}
		i++
	}
	return res 
}
// @lc code=end

