func maxSlidingWindow(nums []int, k int) []int {
	deque := make([]int, 0, k+1)
	res := make([]int, 0, len(nums)-k+1)
	for i := 0; i < len(nums); i++ {
		//fmt.Println("k=", k, "i=", i, "deque:", deque, "len(deque)", len(deque))
		if len(deque) != 0 && deque[0] < i-(k-1) {
			deque = deque[1:]
		}
		for len(deque) != 0 && nums[deque[len(deque)-1]] < nums[i] {
			deque = deque[:len(deque)-1]
		}
		deque = append(deque, i)
		if i >= k-1 {
			res = append(res, nums[deque[0]])
		}
	}
	return res
}