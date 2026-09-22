class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i in range(len(nums) - 1):
            left.append(left[i] * nums[i])

        right = [1]
        for j in range(len(nums) - 1, 0, -1):
            right.append(right[-1] * nums[j])

        opposite = right[::-1]

        output = []
        for k in range(len(nums)):
            output.append(left[k] * opposite[k])
        return output
            