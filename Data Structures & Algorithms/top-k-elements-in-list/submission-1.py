class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        mostFreq = freq.most_common(k)

        result = []
        for number, count in mostFreq:
            result.append(number)
        return result