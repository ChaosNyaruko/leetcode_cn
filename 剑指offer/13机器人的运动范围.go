func getDigitSum (number int) int {
    sum := 0 
    for number > 0 {
        sum += number % 10
        number /= 10
    }
    return sum
}
func movingCount(m int, n int, k int) int {
    if m <=0 || n <= 0 || k < 0 {
        return 0
    }
    visited := make([][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([]bool, n)
    }
    var helper func(int, int) int
    helper = func (x, y int) int {
        if x < 0 || y < 0 || x >= m || y >= n || visited[x][y]{
            return 0
        }
        visited[x][y] = true
        if getDigitSum(x) + getDigitSum(y) > k {
            return 0
        }
        return 1 + helper(x - 1, y) + helper(x + 1,y) + helper(x, y - 1) + helper(x, y+1)
    }
    return helper(0, 0)
}