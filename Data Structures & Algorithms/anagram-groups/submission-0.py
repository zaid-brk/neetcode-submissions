class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        dict = {}
        for str in strs:
            if tuple(sorted(str)) in dict:
                dict[tuple(sorted(str))] += [str]
            else:
                dict[tuple(sorted(str))] = [str]
        return list(dict.values())