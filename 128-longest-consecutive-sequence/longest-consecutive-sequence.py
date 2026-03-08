class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = set()
        for n in nums:
            lcs.add(n)
        
        out = 0
        for i in lcs:
            if i - 1 not in lcs:
                temp = 0
                while (i + temp) in lcs:
                    temp += 1
                out = max(out, temp)
        return out
            
            
        
        