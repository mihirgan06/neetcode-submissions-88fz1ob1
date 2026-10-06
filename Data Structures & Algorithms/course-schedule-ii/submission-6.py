class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
            given: prerequisites
            prerequisites[i] = [a, b] must take coruse b first if you want to take course a

            total of numCourses to take labeled 0 --> numCourses - 1

            return a valid ordering courses you can take to ifnish all courses
            return any of thjem if many valid 
            else return an empty array

            Topological sort:
            build an adjacency list mapping courses --> prerequisites to compelte
            Use a state array to see if there is a cycle
            0,1,2 
            0 --> you havent explored
            1 --> currently exploring
            2 --> finished exploring


        '''
        adj_list = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
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
        return res
        
        
            
            