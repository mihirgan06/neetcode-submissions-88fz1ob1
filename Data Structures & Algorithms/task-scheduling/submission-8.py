import heapq
from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            Given:
            tasks --> tasks[i] = uppercase english character from A --> Z
            also given an integer n
            each cpu cycle --> single task
            CONSTRAINT: identical tasks must be seperated by at least n cycles
            return the min number of CPU cycles required to complete all cycle


            tasks = ["X","X","Y","Y"], n = 2

            X --> Y --> idle --> X --> Y
            Approach:
            we need first to count how many tasks we have using a frequency map (hashmap) --> O(n) iterate all tasks add to hashmap with counts

            we want to execute the task with the highest frequency first
            we can use a heap to store tasks specifically a max heap so that the highest priority task gets executed first
            we can use a queue to hold the taks during cooldown
            FIFO 
            when n cycles we can use the top of the queue

            

        '''
        freq_map = defaultdict(int)

        for task in tasks:
            freq_map[task] += 1

        max_heap = [-freq for freq in freq_map.values()]
        heapq.heapify(max_heap)

        cooldown = deque()
        time = 0

        while cooldown or max_heap:
            time += 1
            if max_heap: #is there a task were allowed to execute
                freq = heapq.heappop(max_heap) #take the most frequent availbel task
                #since we are popping negatives we increment freq

                freq += 1 #once the task becomes 0 its completely executed
                #if the freq isnt 0 it means the task needs to be run again
            #append to the cooldown queue alongside the itme it becomes available again
            #we can do this task at time + n
                if freq != 0:
                    cooldown.append((freq, time + n))
            #check if the earliest waiting task finished cooldown
            if cooldown and cooldown[0][1] == time:
                freq, ready_time = cooldown.popleft()
                #remove the cooled-down task and put it back into the available task heap
                heapq.heappush(max_heap, freq)
        return time


            

        


        


        
        