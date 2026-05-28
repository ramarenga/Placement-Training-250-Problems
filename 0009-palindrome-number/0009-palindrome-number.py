class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindrome
        if x < 0:
            return False

        original = x
        reversed_num = 0

        # Reverse the number
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num