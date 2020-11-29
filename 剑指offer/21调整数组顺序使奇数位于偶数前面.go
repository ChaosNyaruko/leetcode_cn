func exchange(nums []int) []int {
    l := 0
    r := len(nums) - 1
    for l < r {
        for l < r && (nums[l] & 0x1 == 1) {
            l++
        }
        for l < r && (nums[r] & 0x1 == 0) {
            r--
        }
        if l < r {
            nums[l], nums[r] = nums[r], nums[l]
        }
    }
    return nums
}