class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = ''.join(c for c in s if c.isalnum()).lower()
        return parsed == parsed[::-1]