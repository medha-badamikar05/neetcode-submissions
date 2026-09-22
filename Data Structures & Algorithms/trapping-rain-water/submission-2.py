class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        n = len(height)
        leftMax, rightMax = [0] * n, [0] * n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]

        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], height[i])

        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        for j in range(n):
            res += min(leftMax[j], rightMax[j]) - height[j]
        return res




        