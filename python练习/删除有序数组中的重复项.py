class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = {}
        nums2 = nums
        for idx, val in enumerate(nums2):
            if val in a:
                nums[idx] = None
            else:
                a[val] = idx
        while None in nums:
            nums.remove(None)

        return len(nums)


sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
