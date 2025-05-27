# only if you run outside leetcode
# from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth

# only if you run outside leetcode
# print(Solution().maximumWealth([[1,2,3],[3,2,1]]))
