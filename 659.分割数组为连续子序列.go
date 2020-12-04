/*
 * @lc app=leetcode.cn id=659 lang=golang
 *
 * [659] 分割数组为连续子序列
 */

// @lc code=start
type hp struct {
	sort.IntSlice
}

func (h *hp) Pop() interface{} {
	v := h.IntSlice[len(h.IntSlice)-1]
	h.IntSlice = h.IntSlice[:len(h.IntSlice)-1]
	return v
}
func (h *hp) Push(v interface{}) {
	h.IntSlice = append(h.IntSlice, v.(int))
}

func (h *hp) push(v int) {
	heap.Push(h, v)
}
func (h *hp) pop() int {
	return heap.Pop(h).(int)
}

func isPossible(nums []int) bool {
	// key: 以x为子序列末尾元素的x
	// value: 以x为末尾的子序列的长度构成的最小堆
	m := make(map[int]*hp)
	for _, num := range nums {
		if _, ok := m[num]; !ok {
			m[num] = new(hp)
		}
		if mOfNum1, ok := m[num-1]; ok {
			num1Len := mOfNum1.pop()
			if mOfNum1.Len() == 0 {
				delete(m, num-1)
			}
			m[num].push(num1Len + 1)
		} else {
			m[num].push(1)
		}
	}
	for _, length := range m {
		if length.IntSlice[0] < 3 {
			return false
		}
	}
	return true
}

// @lc code=end

