class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
            Given an array of prerequisites where prerequisites[i] = [a,b]
            must take coiurse b before course a
            pair [0,1] meamns you must take course 0 in order to take course 1

            return a valid ordering of ocurses you can take to finishj all courses

            if not possible return emptu array

            return any possible topologicla orderings

            numCourses = 3, prerequisites = [[1,0]]

            res = []
            you must take course 0 before 1
            so append coruse 0 then course 1

            since we need a third course append course 2, which is the next sequential course

            numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

            you need to do course 1 to do course 0
            and you need to do course 2 to do course 1
            you need to do course 0 tod o course 2
            not possible
            cycle



        '''
        res = []
        adj_list = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
        state = [0] * numCourses
        def dfs(course) -> bool:

            if state[course] == 1:
                return False #impossible to finish
            if state[course] == 2:
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
        res.reverse()
        return res
        

            



        