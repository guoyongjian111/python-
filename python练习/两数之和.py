class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        records = dict()
        # 用枚举更方便，就不需要通过索引再去取当前位置的值
        for idx, val in enumerate(nums):
            if target - val not in records:   # 是跟字典里的key进行对比,而不是value
                records[val] = idx
            else:
                return [records[target - val], idx]  # 如果存在就返回字典记录索引和当前索引


a = Solution()
print(a.twoSum([1, 2, 3], 5))
