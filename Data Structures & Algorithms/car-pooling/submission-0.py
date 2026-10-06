class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
            car with capacity empty seats
            the vhicle oonly drives east

            trips[i] = [numPassengers[i], from[i], to[i]]
            indicates the ith trip has numPassengers[i] passangers and the locations to pick them up and drop them off

            true if possible to pick up and drop off all passeners
            trips = [[4,1,2],[3,2,4]], capacity = 4

            4 passnagers pick up at 1 drop off at 2

            3 passengers puck up at 2 drop off at 4

            capacity not exceeded
            the start and end time are significant here
            trips = [[2,1,3],[3,2,4]], capacity = 4
            2 passengers pick up at 1 and drop off at 3
            but we need to pickl up an addiitonal 3 passengers at 2 which overlaps and exceeds the capacity

        '''

        events = []
        for num_passengers, pickup, dropoff in trips:
            events.append([pickup, num_passengers])
            events.append([dropoff, -num_passengers])
        #sort by pickup and drop off time

        events.sort(key = lambda pair: (pair[0], pair[1]))
        current_passengers = 0
        for time, num_passengers in events:
            current_passengers += num_passengers
            if current_passengers > capacity:
                return False
        return True



        