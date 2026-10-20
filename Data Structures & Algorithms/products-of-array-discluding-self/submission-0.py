class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        output = []
        for num in nums:
            output.append(prefix)
            prefix*=num
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *=nums[i]
        return output