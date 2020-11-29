func verifyPostorder(postorder []int) bool {
    if len(postorder) == 0 {
        return true
    }
    root := postorder[len(postorder) - 1]
    i := 0
    for ; i < len(postorder) - 1; i++ {
        if postorder[i] > root {
            break
        }
    }
    j := i
    for ; j < len(postorder) - 1; j++ {
        if postorder[j] < root {
            return false
        }
    }
    left := verifyPostorder(postorder[0:i])
    if !left {
        return false
    }
    return verifyPostorder(postorder[i:j])
}