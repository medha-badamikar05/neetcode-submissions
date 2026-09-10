class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0, n-1
        res = []
        lp = [1]*n
        rp = [1]*n

        while l < n:
            if l != 0:
                lp[l] = lp[l-1] * nums[l-1]
            l += 1
            
        while r >= 0:
            if r != n-1:
                rp[r] = rp[r+1] * nums[r+1]
            r -= 1
        
        for i in range(n):
            res.append(lp[i]*rp[i])
        
        return res
        