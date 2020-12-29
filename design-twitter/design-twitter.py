class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = []
        self.follows = defaultdict(list)
        
​
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets.append([userId, tweetId])
        if userId not in self.follows[userId]:
            self.follows[userId].append(userId)
​
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        ret = []
        idx = len(self.tweets) - 1
        while len(ret) < 10 and idx > -1:
            if self.tweets[idx][0] in self.follows[userId]:
                ret.append(self.tweets[idx][1])
            idx -= 1
            
        return ret
​
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.follows[followerId]:
            self.follows[followerId].append(followeeId)
​
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId != followerId and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
​
​
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
