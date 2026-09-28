class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            given an array of CPIU tasks tasks, where tasks[i] is an uppercase english character from A - Z

            also given an integer n
            at each cpu cucle you can complete a single tasks
            tasks can be completed in any order


            identical tasks must be sperated by at least n cycles



            tasks = ["X","X","Y","Y"], n = 2

            Do task X
            cycle 1
            do task Y
            cycle 2
            break
            cycle 3
            now cooldown expires do 
            cycle 4: X
            cycle 5: you



            we need a heap and hashmap

            hashmap should count the tasks
            for optimal solution we should do the most apparent tasks first
            at each time take the task with the highest remaining frequency that is currently allowed to run







            

        '''

        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        #we now have a mapping of tasks to the amount of times they appear
        max_heap = [-freq for freq in counts.values()]
        heapq.heapify(max_heap)
        time = 0
        cooldown = deque()
        while max_heap or cooldown:
            time += 1
            #pop the task with the highest freq
            if max_heap:
                freq = heapq.heappop(max_heap)
                #since we are popping negatives we increment freq

                freq += 1
                #if the freq isnt 0 it means the task needs to be run again
            #append to the cooldown queue alongside the itme it becomes available again
                if freq != 0:
                    cooldown.append((freq, time + n))
            
            if cooldown and cooldown[0][1] == time:
                freq, ready_time = cooldown.popleft()
                heapq.heappush(max_heap, freq)
        return time
            


            





        



            


        