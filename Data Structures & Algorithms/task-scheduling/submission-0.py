class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks) 
        max_freq = max(counts.values())
        num_max = sum(1 for freq in counts.values() if freq == max_freq) 

        frame_time = (max_freq - 1) * (n + 1) + num_max
        return max(len(tasks), frame_time) 
