class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
            given an array prerequisites, prerequisites[i] = [a,b]
            indicates you must take course b first if you want to take course a


            [0,1] means take coiurse 1 to take course 0


            total of numCourses 


            numCourses = 3, prerequisites = [[1,0]]
            you must take course 0 before course 1
            since numCourses > the amount of courses in prerequistes to finish numCourses courses we must take an additional course

            numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

            you must taek 1 before 0, you must take 2 before 1 but must take 0 before 2


            1 --> 0
            2 --> 1
            0 --> 1
            CYCLE return False


            1. create adjacency list
            2. state array
            if we have state course == 1 return false
            return the topological ordering of courses






        '''

        adj_list = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        state = [0] * numCourses
        res = []


        def dfs(course):
            if state[course] == 1:
                #we cant complete it tehres a cycle
                return False
            if state[course] == 2:
                #we can complete it
                return True
            state[course] = 1
            for nei in adj_list[course]:
                if not dfs(nei):
                    return False
            state[course] = 2
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
                
                

            

            
            

            











