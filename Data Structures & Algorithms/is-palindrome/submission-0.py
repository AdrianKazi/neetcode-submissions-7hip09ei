class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n)
        new_str = ''
        for l in s:
            if l.isalnum():
                new_str += l.lower()
        return new_str == new_str[::-1]

        