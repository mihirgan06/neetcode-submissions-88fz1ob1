class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            you are given an array prerequisites, where prerequisites[i] = [a,b]
            means you must take course b first if you want to take course a

            pair [0,1] indicates you must take course 1 before taking course 0

            total of numCourses courses you are reuqired to take labeldd from 0 to numCourses - 1

            return true if possible to complete all courses else return false


            numCourses = 2, prerequisites = [[0,1]]

            first take course 1 no prerequisites then take course 0

            numCourses = 2, prerequisites = [[0,1],[1,0]]

            we must take course 1 to take course 0
            but to take course 0 to take course 1


            Im instantly thinking this is a graph problem, we can create an adjacnecy list mapping the dependencies


            if we detect a cycle then its false we cant finish all the courses

            we can handle this with a state array

            state array can store 3 possible values 0, 1, 2
            0 ==> havent explored (initialization)
            1 ==> we started exploring
            2 ==> finished
            if we see that a prerequisite for a course is 1
            then we cant complete that course and should return false



        '''

        adj_list = [[] for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            adj_list[course].append(prerequisite)
            #create a list of prerequisties
        
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                #prereq still in progress return false

                return False
            if state[course] == 2:
                #finished exploring this course 
                return True
            state[course] = 1
            for prerequisite in adj_list[course]:
                if not dfs(prerequisite):
                    return False
            state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
                
                
            

        