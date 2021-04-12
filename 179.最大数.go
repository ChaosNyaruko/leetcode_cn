import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

type myInts []int

func (m myInts) Len() int {
	return len(m)
}
func (m myInts) Less(i, j int) bool {
	a, b := strconv.Itoa(m[i]), strconv.Itoa(m[j])

	return a+b > b+a
}
func (m myInts) Swap(i, j int) {
	m[i], m[j] = m[j], m[i]
}

func largestNumber(nums []int) string {
	numstr := myInts(nums)
	sort.Sort(numstr)
	if numstr[0] == 0 {
		return "0"
	}
	return strings.Trim(strings.Replace(fmt.Sprint(numstr), " ", "", -1), "[]")
}
