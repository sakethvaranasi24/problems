class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)

        if len(a) != len(b):
            return False

        if a == b:
            return True
        else:
            return False