class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_array = sorted(nums)

        if sorted_array[0] > 0 or sorted_array[-1] < 0:
            return res


        for i in range(len(sorted_array)):
            l, r = i+1, len(sorted_array)-1
            while l < r:
                s = sorted_array[i] + sorted_array[l] + sorted_array[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    combo = [sorted_array[i], sorted_array[l], sorted_array[r]]
                    if combo not in res:
                        res.append(combo)
                    l += 1
                    r -= 1
                    while sorted_array[l] == sorted_array[l - 1] and l < r:
                        l += 1
        return res



        