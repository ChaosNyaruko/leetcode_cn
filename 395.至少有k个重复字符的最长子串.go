func longestSubstring(s string, k int) int {
    res := 0
    for t := 1; t <=26; t++ {
        noLessThanK, numUnique := 0, 0
        cnt := [128]int{}
        l, r := 0, 0
        for r < len(s) {
            if cnt[s[r] - 'a'] == 0 {
                numUnique++
            }
            cnt[s[r] - 'a']++
            if cnt[s[r] - 'a'] == k {
                noLessThanK++
            }
            for numUnique > t {
                if cnt[s[l] - 'a'] == 1 {
                    numUnique--
                }
                if cnt[s[l] - 'a'] == k {
                    noLessThanK--
                }
                cnt[s[l] - 'a']--
                l++
            }
            if noLessThanK == t {
                res = max(res, r - l + 1)
            }
            r++
        }
    }
    return res
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
