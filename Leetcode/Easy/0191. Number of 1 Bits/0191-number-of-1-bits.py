class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binary = bin(n)[2:].zfill(32)

        for i in binary:
            if i == '1':
                count += 1

        return count

        