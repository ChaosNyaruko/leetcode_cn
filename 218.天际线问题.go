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

func getSkyline_1(buildings [][]int) [][]int {
	if len(buildings) == 0 {
		return nil
	}
	return helper(buildings, 0, len(buildings)-1)
}

// 线扫描法
func getSkyline(buildings [][]int) [][]int {
	// 创建返回值
	var res [][]int
	// 保存所有可能的拐点
	var pairs = make([][2]int, len(buildings)*2) // 切片 类似动态数组
	index := 0
	// 将每一个建筑分成两个部分
	for _, build := range buildings {
		pairs[index][0] = build[0]
		pairs[index][1] = -build[2]
		index++
		pairs[index][0] = build[1]
		pairs[index][1] = build[2]
		index++
	}
	// pairs进行升序
	sort.Slice(pairs, func(i, j int) bool {
		if pairs[i][0] != pairs[j][0] {
			return pairs[i][0] < pairs[j][0]
		}
		return pairs[i][1] < pairs[j][1]
	})
	// 最大堆？
	maxHeap := &IntHeap{}
	// 记录之前的高度
	prev := 0
	// 遍历
	for _, pair := range pairs {
		if pair[1] < 0 {
			heap.Push(maxHeap, -pair[1])
		} else {
			for i := 0; i < maxHeap.Len(); i++ {
				if maxHeap.Get(i) == pair[1] {
					heap.Remove(maxHeap, i)
					break
				}
			}
		}
		top := maxHeap.Top()
		if top != prev {
			res = append(res, []int{pair[0], top})
			prev = top
		}
	}
	return res
}

// Go语言中没有像Java语言一样有这个PriorityQueue类的结构体的，需要自己实现
// 定义堆
type IntHeap []int

func (h IntHeap) Len() int          { return len(h) }
func (h IntHeap) Get(index int) int { return h[index] }
func (h IntHeap) Less(i, j int) bool {
	if i < len(h) && j < len(h) {
		return h[i] > h[j] // > 表示最大堆，< 表示最小堆
	}
	return true
}

func (h IntHeap) Swap(i, j int) {
	if i < len(h) && j < len(h) {
		h[i], h[j] = h[j], h[i]
	}
}

func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }

func (h *IntHeap) Pop() interface{} { // 去掉最后一个数，要注意指针
	old := *h
	l := len(old)
	*h = old[0 : l-1]
	return h
}

func (h IntHeap) Top() int {
	if len(h) != 0 {
		return h[0]
	}
	return 0
}

// @lc code=end

