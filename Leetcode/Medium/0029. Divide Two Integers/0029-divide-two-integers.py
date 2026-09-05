class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:

            temp = divisor
            count = 1

            while dividend >= (temp << 1):
                temp = temp << 1
                count = count << 1

            dividend -= temp
            result += count

        if negative:
            result = -result

        if result > 2**31 - 1:
            return 2**31 - 1

        if result < -2**31:
            return -2**31

        return result