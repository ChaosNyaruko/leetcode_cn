func strStr(haystack string, needle string) int {
	i := 0
	for {
		j := 0
		for {
			if j == len(needle) {
				return i
			}
			if i+j == len(haystack) {
				return -1
			}
			if needle[j] != haystack[i+j] {
				break
			}
			j++
		}
		i++
	}
}
