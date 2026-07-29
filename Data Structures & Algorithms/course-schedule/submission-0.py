class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqMap = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preReqMap[course].append(pre)
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if len(preReqMap[course]) == 0:
                return True
            visit.add(course)
            for pre in preReqMap[course]:
                if not dfs(pre): return False
            visit.remove(course)
            preReqMap[course] = []
            return True 
        for c in range(numCourses):
            if not dfs(c): return False
        return True
        