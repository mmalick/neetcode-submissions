class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = ()
        freqDict = {}
        for number in nums:
            freqDict[number] = freqDict.get(number, 0) + 1
        res = sorted(freqDict, key = freqDict.get, reverse = True)
        return res[:k]