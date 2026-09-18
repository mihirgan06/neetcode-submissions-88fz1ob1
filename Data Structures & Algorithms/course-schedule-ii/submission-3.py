class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
            given array prereqs, prerequisite[i] = [a,b]

            indicates you msut take course b before course a
            total of numCourses courses you are required to take
            return a valid ordering of courses you can take to finish all courses

            numCourses = 3, prerequisites = [[1,0]]
            0 --> 1 --> 2

            topological ordering

            return a valid ordering --> return any of them if not possible return an empty array

        '''
        #build our adjacency list mapping prereq to course

        adj_list = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
        state = [0] * numCourses
        res = []
        def dfs(course):
            if state[course] == 1:
                return False
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


            
        
        