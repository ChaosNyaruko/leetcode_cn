/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */

type NestedIterator struct {
	stk []*NestedInteger
}

func push(stk []*NestedInteger, v *NestedInteger) []*NestedInteger {
	if len(stk) == 0 {
		stk = append(stk, v)
		return stk
	}
	stk = append(stk[:1], stk[0:]...)
	stk[0] = v
	return stk
}
func Constructor(nestedList []*NestedInteger) *NestedIterator {
	return &NestedIterator{nestedList}
}

func (this *NestedIterator) Next() int {
	cur := this.stk[0]
	this.stk = this.stk[1:]
	return cur.GetInteger()
}

func (this *NestedIterator) HasNext() bool {
	for len(this.stk) != 0 {
		cur := this.stk[0]
		if cur.IsInteger() {
			return true
		}
		this.stk = this.stk[1:]
		l := cur.GetList()
		for i := len(l) - 1; i >= 0; i-- {
			this.stk = push(this.stk, l[i])
		}
	}
	return false
}
