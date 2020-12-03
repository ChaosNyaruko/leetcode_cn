func reverseWords(s string) string {
	w := []byte(s)
	reverse(w)
	//fmt.Println(string(w))
	begin, end := 0, 0
	res := ""
	first := false
	for begin < len(w) && end < len(w) {
		for begin = end; begin < len(w) && w[begin] == ' '; begin++ {
			//fmt.Println("begin:",begin, string(w[begin]))
		}
		for end = begin; end < len(w) && w[end] != ' '; end++ {
			//fmt.Println("end:", end, string(w[end]))
		}
		//fmt.Println(begin, end, string(w[begin:end]))
		if begin != len(w) {
			if first {
				res += " "
			}
			res += reverse(w[begin:end])
			first = true
		}
	}
	return res
}
func reverse(word []byte) string {
	w := []byte(word)
	l, r := 0, len(w)-1
	for l < r {
		w[l], w[r] = w[r], w[l]
		l++
		r--
	}
	return string(w)
}