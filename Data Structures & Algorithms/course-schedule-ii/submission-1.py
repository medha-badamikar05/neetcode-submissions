class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return order if len(order) == numCourses else []
