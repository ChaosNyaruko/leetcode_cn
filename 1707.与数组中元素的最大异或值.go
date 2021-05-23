import "math"

const L = 30

type Trie struct {
	childern [2]*Trie
	min      int
}

func (node *Trie) insert(val int) {
	if val < node.min {
		node.min = val
	}
	p := node
	for i := L - 1; i >= 0; i-- {
		bit := (val >> i) & 0x1
		if p.childern[bit] == nil {
			p.childern[bit] = &Trie{min: val}
		}
		p = p.childern[bit]
		if val < p.min {
			p.min = val
		}
	}
}

func (node *Trie) getMaxWithLimit(x, limit int) int {
	if node.min > limit {
		return -1
	}
	p := node
	res := 0
	for i := L - 1; i >= 0; i-- {
		bit := (x >> i) & 0x1
		expected := bit ^ 0x1
		if p.childern[expected] != nil && p.childern[expected].min <= limit {
			res |= (1 << i)
			p = p.childern[expected]
		} else {
			p = p.childern[bit]
		}
	}

	return res
}

func maximizeXor(nums []int, queries [][]int) []int {
	root := &Trie{min: math.MaxInt32}
	for _, num := range nums {
		root.insert(num)
	}

	res := make([]int, len(queries))
	for i, q := range queries {
		res[i] = root.getMaxWithLimit(q[0], q[1])
	}
	return res
}
