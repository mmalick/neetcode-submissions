class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     sortedS = "".join(sorted(s))
        #     sortedT = "".join(sorted(t))
        #     if sortedS == sortedT:
        #         return True
        #     return False
        if len(s) == len(t):
            dictS = {}
            dictT = {}
            for char in s:
                dictS[char] = dictS.get(char, 0) + 1 
            for char in t:
                dictT[char] = dictT.get(char, 0) + 1 
            if dictS == dictT:
                return True
            return False
        return False