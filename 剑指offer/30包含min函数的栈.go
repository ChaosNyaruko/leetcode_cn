type MinStack struct {
	stk []int
    minStk []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{
		stk: make([]int, 0),
		minStk: make([]int, 0),
    }
}


func (this *MinStack) Push(x int)  {
	if len(this.stk) == 0 {
		this.stk = append(this.stk, x)
		this.minStk = append(this.minStk, x)
		return
	}
	top := this.minStk[len(this.minStk) - 1] 
	if x < top {
		this.minStk = append(this.minStk, x)
	} else {
		this.minStk = append(this.minStk, top)
	}
	this.stk = append(this.stk, x)
}


func (this *MinStack) Pop()  {
	this.stk = this.stk[:len(this.stk) - 1]
	this.minStk = this.minStk[:len(this.minStk) - 1]
}


func (this *MinStack) Top() int {
	return this.stk[len(this.stk) - 1]
}


func (this *MinStack) GetMin() int {
	return this.minStk[len(this.minStk) - 1]
}
