class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)

        result = []

        for num, count in nums_count.items():
            if count >= k:
                result.append(num)
        
        return result