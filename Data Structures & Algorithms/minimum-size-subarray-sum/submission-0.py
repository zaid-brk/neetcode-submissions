class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        tot = 0

        for r in range(len(nums)):
            tot += nums[r]

            while tot >= target:
                res = min(res, (r - l + 1))
                tot -= nums[l]
                l += 1

        return res if res != float('inf') else 0