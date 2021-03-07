func isPalindrome(s string) bool {
    l, r := 0, len(s)-1
    for l < r {
        if s[l] != s[r] {
            return false
        }
        l++
        r--
    }
    return true
}
func partition(s string) [][]string {
    res := [][]string{}
    path := make([]string, 0)
    var helper func(int)
    helper = func(left int) {
        if left == len(s) {
            tmp := make([]string, len(path))
            copy(tmp, path)
            res = append(res, tmp)
            return
        }
        for right := left;  right < len(s); right++ {
            if isPalindrome(s[left:right+1]) {
                path = append(path, s[left:right+1])
                helper(right + 1)
                path = path[:len(path) - 1]
            }
        }
    }
    helper(0)
   // fmt.Println(path)
    return res
}
