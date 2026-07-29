class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n

        i = 1
        j = n-2

        while i < n:
            pref[i] = pref[i-1] * nums[i-1]
            i += 1
        
        while j >= 0:
            suff[j] = suff[j+1] * nums[j+1]
            j -= 1

        res = []
        for x in range(n):
            res.append(pref[x] * suff[x])
        return res

