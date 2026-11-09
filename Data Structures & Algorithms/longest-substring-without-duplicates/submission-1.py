class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        max_len = 0
        l, r = 0, 0
        while r < len(s):
            sequence = s[l:r]
            if s[r] in sequence:
                l= cache[s[r]]+1
            else:
                max_len = max(max_len, r-l+1)
            cache[s[r]] = r
            r+=1
        return max_len


