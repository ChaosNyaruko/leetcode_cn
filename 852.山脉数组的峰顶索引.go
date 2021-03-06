func peakIndexInMountainArray(arr []int) int {
	l, r := 0, len(arr)-1
	for l < r {
		m := l + (r-l)/2
		if arr[m] > arr[m+1] {
			r = m
		} else {
			l = m + 1
		}
	}
	return l
}
