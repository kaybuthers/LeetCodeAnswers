class Solution:
    def isPalindrome(self, x: int) -> bool:
      return str(x) == str(x)[::-1]

# Only if outside leetcode
# Solution().isPalindrome(-121)
