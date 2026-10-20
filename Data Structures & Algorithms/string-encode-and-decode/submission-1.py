class Solution:

    def encode(self, strs: List[str]) -> str:
        stringTotal = ""
        for s in strs:
            stringTotal += str(len(s)) + "$" + s
        return stringTotal
    def decode(self, s: str) -> List[str]:
        i = 0
        listOfStrings = []
        while i < len(s):
            separator = s.find("$", i)
            length = int(s[i:separator])
            string = s[separator+1:separator + 1 + length]
            listOfStrings.append(string)
            i = separator + length + 1
        return listOfStrings