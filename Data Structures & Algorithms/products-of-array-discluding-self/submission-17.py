class Solution:
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = int(math.prod(nums))
        res = []
        for i in range(len(nums)):
            if nums[i] != 0:
                res.append(int(product/nums[i]))
            else:
                res.append(int(math.prod(nums[:i] + nums[i+1:])))
        return res
        