class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = []

        for l in s:
            l = l.lower()
            if l != ' ' and (l.isalpha() or l.isdigit()):
                clean_s.append(l)

        print(clean_s)
        return clean_s == clean_s[::-1]