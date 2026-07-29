class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqSet = set(nums)
        longest = 0

        for num in nums:
            # check if num is the start of a sequence
            pre = num - 1 
            if pre not in seqSet:
                currentLen = 1
                succ = num + 1
                while succ in seqSet:
                    currentLen += 1
                    succ += 1
                longest = max(longest, currentLen)
        return longest