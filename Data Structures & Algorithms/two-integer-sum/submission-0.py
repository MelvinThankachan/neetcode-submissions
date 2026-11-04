class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in nums_hash:
                return [nums_hash[need], i]

            nums_hash[num] = i
