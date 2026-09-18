class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            given an array prerequisites, where prerequisites[i] = [a,b]
            indicates you must take course b first then take course a


            pair [0,1] indicates take course 1 before course 0

            total of numCourses courses you are reqired to take

            0 --> numCourses - 1
            numCourses = 2, prerequisites = [[0,1]]
            true, you do 1 then 0 and finish 2 courses


            numCourses = 2, prerequisites[[0,1], [1,0]]
            do course 1 to do course 0

            then you need to do course 0 to do 1

            each is a prerequistie for the other --> return false its not possible to finish both courses
            return false

            Approach:
            - build an adjacency list mapping prerequisite to course
            - we need a state array of 3 possilbe values
            - 0, 1, 2
                0 == we havent started exploring
                1 == currently exploring
                2 == finished expliring
            - detect cycle if we see 1 then we should return false
        '''
        adj_list = [[] for i in range(numCourses)]

        for prereq, course in prerequisites:
            adj_list[prereq].append(course)
            #point a prereq --> course
            #adj_list[1] = 0 we need to take 1 as a prerequisite for 0
        state = [0] * numCourses #for each course in numCourses we store 1 of 3 states
        def dfs(course):
            if state[course] == 1:
                #it means we detect a cycle so return false
                return False
            if state[course] == 2:
                #finished exploring this course 
                return True
            state[course] = 1
            for nei in adj_list[course]:
                if not dfs(nei):
                    return False
            state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
