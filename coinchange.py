import sys
import unittest


class Solution:
    def coinChange(self, coins, amount):
        """

        :param coins: List[int]
        :param amount: int
        :return: int
        """

        # DP + memoization
        # The idea was try to find the combination sum of smallest value and then add up to large value.
        dp = [0] + [amount + 1] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]

        # lowest = self.recursive(coins, amount, 0)
        # return -1 if lowest == sys.maxsize else lowest

    # originally, this was my first idea. i tried to do Backtracking without collect all of result.
    def recursive(self, coins, amount, count):
        if amount == 0:
            return count
        if amount < 0:
            return sys.maxsize
        lowest = sys.maxsize
        for coin in coins:
            lowest = min(lowest, self.recursive(coins, amount - coin, count + 1))
        return lowest


# solution = Solution()
# print(solution.coinChange([1, 2, 5], 11))

class coinChangeTestCases(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        answer = solution.coinChange([1, 2, 5], 11)
        self.assertEqual(3, answer)

    def test_2(self):
        solution = Solution()
        answer = solution.coinChange([1, 2, 7, 9, 11], 25)
        self.assertEqual(3, answer)

    def test_3(self):
        solution = Solution()
        answer = solution.coinChange([1, 2, 7, 9, 11], 14)
        self.assertEqual(2, answer)

    def test_4(self):
        solution = Solution()
        answer = solution.coinChange([7, 9], 20)
        self.assertEqual(-1, answer)

    def test_5(self):
        solution = Solution()
        answer = solution.coinChange([7, 9], 0)
        self.assertEqual(0, answer)

    def test_6(self):
        solution = Solution()
        answer = solution.coinChange([3, 5], 21)
        ## dry run
        # start with coin 3
        # dp[3] = 1
        # dp[6] = 2
        # dp[9] = 3
        # dp[12] = 4
        # dp[15] = 5
        # dp[18] = 6
        # dp[21] = 7
        # start with coin 5
        # dp[5] = 1
        # dp[6] = min(2, dp[1] + 1)
        # dp[6] = min(2, 22)
        # dp[6] = 2
        # dp[10] = 2
        # dp[11] = min(22, dp[11-5] + 1)
        # dp[11] = min(22, 2 + 1)
        # dp[11] = 3
        # dp[15] = 3
        # dp[16] = min(22, dp[16-5] + 1)
        # dp[16] = min(22, dp[11] + 1)
        # dp[16] = min(22, 3 + 1)
        # dp[16] = 4
        # dp[20] = 4
        # dp[21] = min(7, dp[21-5] + 1)
        # dp[21] = min(7, dp[16] + 1)
        # dp[21] = min(7, 5)
        # dp[21] = 5
        self.assertEqual(5, answer)
