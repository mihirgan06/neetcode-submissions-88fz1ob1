class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #given array of tasks, where tasks[i] is an uppercase eng char from A-Z
        import heapq
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        #now we know how often each letter shows up
        

        heap = [- cnt for cnt in freq.values()]
        heapq.heapify(heap)
        #highest priority elements at the front of the array

        time = 0
        q = deque()

        while heap or q:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        return time


        