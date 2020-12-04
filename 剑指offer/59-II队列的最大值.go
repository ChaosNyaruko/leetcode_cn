type MaxQueue struct {
	deque []int
	queue []int
}

func Constructor() MaxQueue {
	return MaxQueue{
		deque: make([]int, 0),
		queue: make([]int, 0),
	}
}

func (this *MaxQueue) Max_value() int {
	if len(this.deque) == 0 {
		return -1
	}
	return this.deque[0]
}

func (this *MaxQueue) Push_back(value int) {
	for len(this.deque) > 0 && value >= this.deque[len(this.deque)-1] {
		this.deque = this.deque[:len(this.deque)-1]
	}
	this.deque = append(this.deque, value)
	this.queue = append(this.queue, value)
}

func (this *MaxQueue) Pop_front() int {
	if len(this.queue) == 0 {
		return -1
	}
	res := this.queue[0]
	this.queue = this.queue[1:]
	if res == this.deque[0] {
		this.deque = this.deque[1:]
	}
	return res
}

/**
 * Your MaxQueue object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Max_value();
 * obj.Push_back(value);
 * param_3 := obj.Pop_front();
 */