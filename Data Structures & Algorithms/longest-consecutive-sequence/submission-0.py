class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setS = set(nums)
        longestSeq = 0
        for i in setS:
            if i -1 not in setS:
                currentSeq = 1
                nextNum = i + 1
                while nextNum in setS:
                    currentSeq += 1
                    nextNum += 1
                longestSeq = max(currentSeq,longestSeq)
        return longestSeq