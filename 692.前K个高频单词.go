import "container/heap"

type pair struct {
	w string
	c int
}
type hp []pair

func (h hp) Len() int {
	return len(h)
}

func (h hp) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h hp) Less(i, j int) bool {
	a, b := h[i], h[j]
	if a.c == b.c {
		return a.w > b.w
	}
	return a.c < b.c
}

func (h *hp) Pop() interface{} {
	a := *h
	v := a[len(a)-1]
	*h = a[:len(a)-1]
	return v
}
func (h *hp) Push(v interface{}) {
	*h = append(*h, v.(pair))
}

func topKFrequent(words []string, k int) []string {
	cnt := make(map[string]int)
	for _, word := range words {
		cnt[word]++
	}
	h := &hp{}
	for w, c := range cnt {
		heap.Push(h, pair{w, c})
		if h.Len() > k {
			heap.Pop(h)
		}
	}
	res := make([]string, k)
	for i := 0; i < k; i++ {
		v := heap.Pop(h).(pair)
		// fmt.Println(v)
		res[k-i-1] = v.w
	}
	return res
}
