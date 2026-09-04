class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # count = 1
        # for i in range(1,len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[count] = nums[i]
        #         count += 1
        # return count
        unique = sorted(list(set(nums)))

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)
        