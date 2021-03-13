type node struct {
    val int
    next *node
}
type MyHashSet struct {
    set []*node
}

func hash(key int) int {
    return key % 769
}
/** Initialize your data structure here. */
func Constructor() MyHashSet {
    ret := MyHashSet {
        set: make([]*node, 769),
    }
    for i := range ret.set {
        ret.set[i] = &node{val: -1}
    }
    return ret
}


func (this *MyHashSet) Add(key int)  {
    slot := hash(key)
    prev := this.set[slot]
    p := prev.next
    for ; p != nil && p.val != key; p = p.next{
        prev = p
    }
    if p == nil {
        prev.next = &node{val: key}
    }
}


func (this *MyHashSet) Remove(key int)  {
    slot := hash(key)
    prev := this.set[slot]
    p := prev.next
    for ;p != nil; p = p.next {
        if p.val == key {
            prev.next = p.next
        }
        prev = p
    }
}


/** Returns true if this set contains the specified element */
func (this *MyHashSet) Contains(key int) bool {
    slot := hash(key)
    prev := this.set[slot]
    p := prev.next
    for ; p != nil; p = p.next {
        if p.val == key {
            return true
        }
    }
    return false
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
