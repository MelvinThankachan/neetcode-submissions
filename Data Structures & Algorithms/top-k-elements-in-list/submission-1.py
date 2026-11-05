class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)

        priority_queue = []

        for num, count in nums_count.items():
            heapq.heappush(priority_queue, (count * -1, num))
        
        result = []

        for _ in range(k):
            count, num = heapq.heappop(priority_queue)
            result.append(num)
        
        return result


