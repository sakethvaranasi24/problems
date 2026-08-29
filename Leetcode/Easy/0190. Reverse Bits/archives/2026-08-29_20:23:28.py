class Solution:
    def reverseBits(self, n: int) -> int:

        binary = bin(n)[2:].zfill(32)
        
        a = binary[::-1]
       
        return int(a,2)