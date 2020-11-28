type CQueue struct {
    stkIn []int
    stkOut []int
}

func Constructor() CQueue {
    return CQueue{
        stkIn: make([]int, 0),
        stkOut: make([]int, 0),
    }
}


func (this *CQueue) AppendTail(value int)  {
    this.stkIn = append(this.stkIn, value)
}


func (this *CQueue) DeleteHead() int {
    if len(this.stkOut) != 0 {
        res := this.stkOut[len(this.stkOut) - 1]
        this.stkOut = this.stkOut[:len(this.stkOut) - 1]
        return res
    }
    for len(this.stkIn) != 0 {
        this.stkOut = append(this.stkOut, this.stkIn[len(this.stkIn) - 1])
        this.stkIn = this.stkIn[:len(this.stkIn) - 1]
    }    
    if len(this.stkOut) != 0 {
        res := this.stkOut[len(this.stkOut) - 1]
        this.stkOut = this.stkOut[:len(this.stkOut) - 1]
        return res
    }
    return -1
}


/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */