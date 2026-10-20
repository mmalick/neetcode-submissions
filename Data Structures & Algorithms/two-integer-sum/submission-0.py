class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        for i,element in enumerate(nums):
            if target - element in sumDict:
                return [sumDict[target-element],i]
            sumDict[element] = i
            