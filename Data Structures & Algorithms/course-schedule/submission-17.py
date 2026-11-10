class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            Given an array prerequisites
            prerequities[i] = [a,b] --> must take course b first to take course a

            [0,1] --> must take course 1 before course 0
            total of numCourses to take
            return true if possible to complete all courses
            else return false

            numCourses = 2, prerequisites = [[0,1]]

            take cours 1 then 0
            2 courses completed

            numCourses = 2, prerequisites = [[0,1],[1,0]]

            to take course 0 must take course 1, but to take course 1 must take course 0
            so cycle

            if we detect a cycle its impossible to complete all courses




        '''
        adj_list = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        state = [0] * numCourses
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
