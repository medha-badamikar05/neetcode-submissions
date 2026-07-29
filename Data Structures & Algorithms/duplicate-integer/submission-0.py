class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        duplicate = set()

        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate.add(num)
        return False

        