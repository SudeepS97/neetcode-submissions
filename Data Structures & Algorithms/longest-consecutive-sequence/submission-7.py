class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tracking = defaultdict(int)
        for n in sorted(nums):
            tracking[n] = tracking.get(n-1, 0) + 1
        return max(tracking.values())
        