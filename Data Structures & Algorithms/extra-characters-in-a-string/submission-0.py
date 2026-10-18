class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        memo = {}

        def dfs(i): 
            if i == len(s):
                return 0
            if i in memo: 
                return memo[i]
            
            min_extra = float('inf')
            extra_chars = 1 + dfs(i + 1)

            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_set:
                    min_extra = min(min_extra, dfs(j))

            result = min(extra_chars, min_extra)
            memo[i] = result
            return result

        return dfs(0)