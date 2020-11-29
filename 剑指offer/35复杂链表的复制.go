/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {
    p := head
    for p != nil {
        copy := &Node{p.Val, p.Next, nil}
        p.Next = copy
        p = copy.Next
    }
    p = head
    for p != nil {
        if p.Random == nil {
            p.Next.Random = nil
        } else {
            p.Next.Random = p.Random.Next
        }
        p = p.Next.Next
    }

    p = head
    res := p
    if p == nil {
        res = nil
    } else {
        res = p.Next
    }
    for p != nil {
        copy := p.Next
        p.Next = copy.Next
        if p.Next != nil {
            copy.Next = p.Next.Next
        } else {
            copy.Next = nil
        }
        p = p.Next
    }
    return res
}