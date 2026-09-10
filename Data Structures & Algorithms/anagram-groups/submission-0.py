class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            alphabetList = [0] * 26
            for c in string:
                alphabetList[ord(c) - ord("a")] += 1

            anagrams[tuple(alphabetList)].append(string)

        return list(anagrams.values())