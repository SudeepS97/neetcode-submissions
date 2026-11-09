class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        out = ""
        for s in strs:
            out+=f'{len(s)}|{s}'
        return out

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "|":
                j += 1
            string_length = int(s[i:j])
            i = j+1
            j = i+string_length
            res.append(s[i:j])
            i=j
        return res