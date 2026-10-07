class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedNum = 0
        original = x
        if x < 0:
            return False
        while x > 0:
            digit = x % 10
            reversedNum = reversedNum * 10 + digit
            x //= 10
        return reversedNum == original