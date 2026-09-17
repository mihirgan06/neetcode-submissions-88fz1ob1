class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            given an array prerequisites, prerequisites[i] = [a.b] means you must frist take course b to take course a

            [0,1] take course 1 before course 0



            total of numCourses you take 0 --> numCourses - 1

            return true if it is possible to finish all courses, otherwise return fasle

            numCourses = 2, prerequisites = [[0, 1]]
            true

            numCourses = 2, prequisites = [[0, 1],[1,0]]
            directed


        '''
        adj_list = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
        
        visited = set()
        state = [0] * numCourses


        def dfs(course):
            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            state[course] = 1
            for neighbor in adj_list[course]:
                 if not dfs(neighbor):
                    return False
            
            state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

            


        





            
