class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            dictS = {}
            for char in s:
                dictS[char] = dictS.get(char, 0) + 1
            key = tuple(sorted(dictS.items()))
            groups[key] = groups.get(key, []) + [s]
        return list(groups.values())