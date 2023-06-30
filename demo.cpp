#include <bits/stdlib++>

class Solution
{
public:
    long long dp[46] = {-1};

    int climbStairs(long n)
    {
        if (dp[n] != -1)
            return dp[n];
        if (n == 0)
            return 1;
        long step1 = 0, step2 = 0;
        step1 = climbStairs(n - 1);
        if (n > 1)
            step2 = climbStairs(n - 2);
        dp[n] = step1 + step2;
        return step1 + step2;
    }
};
int main(int argc, char const *argv[])
{
    Solution s1;
    cout << s1.climbStairs(5);
    return 0;
}
