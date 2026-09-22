class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            letter = s[right]

            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

            window_length = right - left + 1
            most_common = max(counts.values())

            while window_length - most_common > k:
                counts[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                most_common = max(counts.values())

            longest = max(longest, window_length)

        return longest