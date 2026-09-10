class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = []

        for string in strs:
            encodedString.append(str(len(string)))
            encodedString.append("#")
            encodedString.append(string)
        return "".join(encodedString)

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
    
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i+length
            decodedStrings.append(s[i:j])
            i = j
            
        return decodedStrings
