/*
 * @lc app=leetcode.cn id=494 lang=golang
 *
 * [494] 目标和
 */

// @lc code=start
func findTargetSumWays(nums []int, S int) int {
	sum := 0
	n := len(nums)
	if n == 0 {
		return 0
	}
	for _, num := range nums {
		sum += num
	}

	if S > sum {
		return 0
	}

	target, odd := (S+sum)/2, (S+sum)%2
	if odd == 1 {
		return 0
	}
	// fmt.Println("target:", target)
	// 转化成为组成target的0，1背包问题
	// dp[i][j]表示考虑0~i-1的物品，目标为j时的方案数
	// f(k,C) = f(k-1, C)+f(k-1,C-num[i])
	dp := make([][]int, n)
	for i, _ := range dp {
		dp[i] = make([]int, target+1)
	}

	// base
	dp[0][0] = 1
	for j := 0; j <= target; j++ {
		if nums[0] == j {
			dp[0][j] += 1
		}
	}
	for i := 1; i < n; i++ {
		for j := 0; j <= target; j++ {
			dp[i][j] += dp[i-1][j]
			if j >= nums[i] {
				//	fmt.Println("j-nums[i]", j-nums[i])
				dp[i][j] += dp[i-1][j-nums[i]]
			}
		}
	}
	return dp[n-1][target]
}

// @lc code=end

/*
	int findTargetSumWays(vector<int>& nums, int S) {
		int n = nums.size();
		int sum = accumulate(nums.begin(), nums.end(), 0);
		if (sum < S) return 0;
		vector<vector<int>> memo(n, vector<int>(2 * sum + 1, 0));

		//f(k,C) = max(f(k-1, target-a[i]), f(k-1, target+a[i]))
		for (int i = 0; i <= 2 * sum ; i++) {
			memo[0][i] += (nums[0] == i-sum )? 1 : 0;
			memo[0][i] += (-nums[0] == i - sum) ? 1 : 0;
		}
		for (int i = 1; i<n; i++) {
			for (int j = 0; j <= 2 * sum; j++) {
				if (j + nums[i] <= 2 * sum) {
					memo[i][j] += memo[i - 1][j - sum + nums[i] + sum];
				}
				if (j - nums[i] >= 0) {
					memo[i][j] += memo[i - 1][j - sum - nums[i] + sum];//, memo[i][j];
				}
			}
		}
		return memo[n - 1][S + sum];
	}
*/

