class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch.lower()

        reverse_string = new[::-1]

        if new == reverse_string:
            return True
        else:
            return False
   
        