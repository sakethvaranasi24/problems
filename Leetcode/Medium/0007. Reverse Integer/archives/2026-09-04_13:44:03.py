class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(abs(x))
            s = s[::-1]
            result = -int(s)
        
        else:
            s = str(x)
            s = s[::-1]
            result =  int(s)

        if result < -2 ** 31 or result > 2 ** 31-1:
            return 0
        return result