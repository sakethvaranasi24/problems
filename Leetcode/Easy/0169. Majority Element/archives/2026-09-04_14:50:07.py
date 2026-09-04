class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        kl = 0
        for i in nums:
            if count == 0:
                kl = i
            if i == kl:
                count += 1
            else:
                count -= 1

        return kl
        