class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < k+1:
            return len(s)

        counts = defaultdict(int)
        max_len = k+1
        most_common_count = 0
        l = 0

        for i in range(len(s)):
            counts[s[i]] += 1
            most_common_count = max(most_common_count, counts[s[i]])
            while i - l + 1 - most_common_count > k:
                counts[s[l]] -= 1
                l += 1
            max_len = max(max_len, i - l + 1)
        return max_len
            