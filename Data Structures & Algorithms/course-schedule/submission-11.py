class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            given an array prerequisites where prerequisites[i] = [a,b]

            indicates you must take b then take a


            pair [0,1] means take course 1 in order to take course 0

            return True if its possible to finish all courses otherwise return false


            ex:
            numCourses = 2, prerequisites = [[0,1]]
            take course 1 (course 1)
            then take course 0 (course 2)
            this returns true because we successfuilly complete all the prerequites and courses and we only take 2 courses

            numCourses = 2, prerequisites = [[0,1],[1,0]]

            try to take course 1 to take course 0 
            but we must take course 0 in order to take course 1

            return false --> cycle detected thus impossible to complete 2 courses
            we just need a mapping of course --> prerequisite

            hold a state array with states 0, 1, 2
            0 = base value havent started exploring
            1 = currently exploring
            2 = finished
        '''

        adj_list = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
        state = [0] * numCourses

        def dfs(course):

            if state[course] == 1:
                return False
            #we need to detect cycle
            if state[course] == 2:
                #we can successfully complete that course
                return True
            state[course] = 1
            #we are currently processing our course 
            for nei in adj_list[course]:
                if not dfs(nei):
                    return False
            state[course] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
            


        