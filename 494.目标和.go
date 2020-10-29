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
1. 都是类似给你元素和目标，从元素中选取组合达到目标，我觉得这样的问题，都可以归类到背包问题里。
2.  dp[i][j]表示到第i个字符和为j的方法数。
    dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
    dp[i - 1][j - nums[i]] 表示这次是+时的方法数，
    dp[i - 1][j + nums[i]] 表示这次是-时的方法数。
    如果我们j正序遍历，把dp数组初始化为0.
    则上面公式可以转化为：dp[i][j] == 0(计算前)
    dp[i][j] = dp[i][j] + dp[i - 1][j - nums[i]]
    dp[i][j] = dp[i][j] + dp[i - 1][j + nums[i]] ==>
    遍历j时，我们利用上一次dp[i- 1][x]的计算结果，可以每次更新两个dp[i][x]的结果：
    dp[i][j + nums[i]] = dp[i][j + nums[i]] + dp[i - 1][j]; 此时dp[i][j + nums[i]] = 0
    dp[i][j - nums[i]] = dp[i][j - nums[i]] + dp[i - 1][j]; 此时dp[i][j - nums[i]] = 0 =>
    编程如下形式：
    dp[i][j + nums[i]] += dp[i - 1][j]
    dp[i][j - nums[i]] += dp[i - 1][j]
    这样，每次遍历j时，我们不计算dp[i][j]的值，而是利用dp[i - 1][j]的值，更新两个相关dp节点的值，会加速计算
*/

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

