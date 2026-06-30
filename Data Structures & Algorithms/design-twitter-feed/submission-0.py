from collections import defaultdict
import heapq

class Twitter:
    '''
        Implement a simplified twitter which allows users to post, follow/unfollow, and view the 10 most recent tweets 

        Users and tweets are uniquely identified by their IDs
        Input:
        ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
        Output:
        [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]
        Explanation:
        Twitter twitter = new Twitter();-
        twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
        twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
        twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
        twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
        twitter.follow(1, 2);     // User 1 follows user 2.
        twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
        twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
        twitter.unfollow(1, 2);   // User 1 unfollows user 2.
        twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
        


    '''


    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) #user id --? lsit of [count, tweetIDs]
        self.followMap = defaultdict(set) #userID --> set of followeeID


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] #ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:

                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)