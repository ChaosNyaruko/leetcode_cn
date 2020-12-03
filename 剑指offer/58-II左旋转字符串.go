func reverseLeftWords(s string, n int) string {
	w := []byte(s)
	reverse(w[0:n])
	reverse(w[n:])
	reverse(w)
	return string(w)
}
func reverse(w []byte) {
	l, r := 0, len(w)-1
	for l < r {
		w[l], w[r] = w[r], w[l]
		l++
		r--
	}
}