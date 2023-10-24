class Twitter:

    def __init__(self):
        self.count = 0
        self.mapTweet = defaultdict(list) # userID : [time/count , tweet]
        self.mapFollowers = defaultdict(set) # follower : followee

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.mapTweet[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = [] # 10 most recent tweet ids (based off count)

        minheap = []
        self.mapFollowers[userId].add(userId)
        # add any tweets from followed/self
        for followeeId in self.mapFollowers[userId]:
            if followeeId not in self.mapTweet:
                continue
            
            index = len(self.mapTweet[followeeId]) - 1 # give us last index (or most recent)
            count, tweet = self.mapTweet[followeeId][index]
            minheap.append([count,tweet,followeeId,index-1]) 
            # pass in followee and index to get their next recent tweet
        
        heapq.heapify(minheap)

        while minheap and len(result) < 10:
            count,tweet,followeeId,index = heapq.heappop(minheap)
            result.append(tweet)

            # search for more tweets
            if index >= 0:
                count,tweet = self.mapTweet[followeeId][index]
                heapq.heappush(minheap,[count,tweet,followeeId,index-1])

             
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.mapFollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.mapFollowers[followerId]:
            self.mapFollowers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
