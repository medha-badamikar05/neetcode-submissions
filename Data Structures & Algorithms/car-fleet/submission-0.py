class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posToSpeedMap = {}

        for i in range(len(position)):
            posToSpeedMap[position[i]] = speed[i]
        
        posToSpeedMap = dict(sorted(posToSpeedMap.items(), reverse=True))
        stack = []

        for p,s in posToSpeedMap.items():
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

