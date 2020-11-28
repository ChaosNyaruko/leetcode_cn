func replaceSpace(s string) string {
	if len(s) == 0 {
		return  ""
	}
	numSpace := 0 
    for _, c := range s {
        if c == ' ' {
			numSpace++
		}
	}
	res := make([]byte, len(s) + 2 * numSpace)
	p1 := len(s) - 1
	p2 := len(res) - 1
	for ; p1 >= 0; p1-- {
		if s[p1] != ' ' {
			res[p2] = s[p1]
			p2--
		} else {
			res[p2] = '0'
			res[p2 -1]='2'
			res[p2-2] = '%'
			p2 -= 3
		}
	}
	return string(res)
}