class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
            given a network of n directed nodes, labeled from 1 --> n

            also given times, list of directed edges where
            times[i] = (ui, vi, ti)
            ui = source
            vi = target
            ti = time (weight)

            also given k --> we will send a singal from
            return the min time it takes for all the n nodes to receive the signal 


            times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

            the min time for 4 nodes to receive the ignal

            times = [[1,2,1],[2,3,1]], n = 3, k = 2

            the time it takes for 3 nodes to receive a singl of 2



            time = [source, target, weight of the edge]
            the weight is the amount of time it takes to go from the source to the target

            k is our starting node


            starting from k how long would it take to send. asignal form k to every noide, 
            if its disconnected --> return -1 its not posssible




            BFS algorithm
            use a heap for min distance

            E(logV)

        '''

        #given list of edges make an adjacency list first


        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
            #for every starting edge store every target node and the weight

        #add the signal (first node) and the weight which is initially 0
        minHeap = [(0, k)]

        visit = set()
        t = 0


        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            #we dont want to revisit a visited node
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                #for every non-visited neighbor or n1
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
                    #add the weight and the node
        return t if len(visit) == n else -1


            




