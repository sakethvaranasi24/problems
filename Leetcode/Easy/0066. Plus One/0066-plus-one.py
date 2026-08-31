class Solution:
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        digits = digits[:-1]

        if len(digits) == 0:
            return [1, 0]

        result = self.plusOne(digits)

        return result + [0]