class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        res = [-1, -1]
        if n < 2:
            return res
        map = {}
        res = [-1, -1]
        for i in range(n):
            diff =  target - nums[i]
            if diff in map and map[diff] != i:
                res[0] = map[diff]
                res[1] = i
            map[nums[i]] = i
        return res