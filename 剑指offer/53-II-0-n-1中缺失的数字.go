func missingNumber(nums []int) int {
    l := 0
    r := len(nums) - 1
    for l < r {
        m := l + (r - l) /2
        if nums[m] == m  {
            l = m + 1
        }  else {
            r = m
        }
    }
    if nums[l] == l {
        return l + 1
    }
    return nums[l] - 1
}
