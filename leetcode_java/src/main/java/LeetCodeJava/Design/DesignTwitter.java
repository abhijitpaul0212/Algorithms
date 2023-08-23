package LeetCodeJava.Design;

// https://leetcode.com/problems/design-twitter/

import javafx.util.Pair;

import java.util.*;

public class DesignTwitter {

    // V0
    // TODO : fix below
//    class Twitter {
//
//        // attr
//        PriorityQueue<Integer> post_queue; // <time1, time2..> // priority queue (small heap)
//        HashMap<Integer, List<Integer>> posts; // <time, [user_id, twitter_id]>
//        HashMap<Integer, List<Integer>> following; // <user, user's following>
//
//        int _time;
//
//
//        // constructor
//        public Twitter() {
//            this.post_queue = new PriorityQueue();
//            this.posts = new HashMap<>();
//            this.following = new HashMap<>();
//            this._time = 0;
//        }
//
//        public void postTweet(int userId, int tweetId) {
//            List<Integer> _cur = new ArrayList<>();
//            _cur.add(userId);
//            _cur.add(tweetId);
//            this.posts.put(this._time, _cur);
//            this.post_queue.add(this._time);
//            this._time += 1;
//        }
//
//        public List<Integer> getNewsFeed(int userId) {
//            int cnt = 10;
//            // get following list
//            List<Integer> _following = this.following.get(userId);
//            PriorityQueue pq = this.post_queue;
//            List<Integer> res = new ArrayList<>();
//            // get smallest time at each remove
//            while (pq.size() > 0 || cnt > 0){
//                Integer _post_time = (Integer) pq.remove();
//                List<Integer> uid_tid = this.posts.get(_post_time);
//                if (_following.contains(uid_tid.get(0))){
//                    res.add(uid_tid.get(1));
//                    cnt -= 1;
//                }
//
//            }
//
//            return res;
//        }
//
//        public void follow(int followerId, int followeeId) {
//            if (!this.following.containsKey(followerId)){
//                this.following.put(followerId, new ArrayList<>());
//            }else{
//                List<Integer> followees = this.following.get(followerId);
//                followees.add(followeeId);
//                this.following.put(followerId, followees);
//            }
//        }
//
//        public void unfollow(int followerId, int followeeId) {
//            if(this.following.containsKey(followerId)){
//                List<Integer> followees = this.following.get(followerId);
//                int idx = followees.indexOf(followeeId);
//                followees.remove(idx);
//                this.following.put(followerId, followees);
//            }
//        }
//    }

    // V1
    // https://leetcode.com/problems/design-twitter/solutions/2720611/java-simple-hashmap-stack/
    class Twitter_1 {
        Stack<Pair<Integer,Integer>> tweets;
        HashMap<Integer, Set<Integer>> network;

        public Twitter_1() {
            tweets = new Stack<>();
            network = new HashMap<>();
        }

        public void postTweet(int userId, int tweetId) {
            tweets.push(new Pair(userId, tweetId));
        }

        public List<Integer> getNewsFeed(int userId) {
            Stack<Pair<Integer, Integer>> store = new Stack<>();
            List<Integer> ans = new ArrayList<>();
            Set<Integer> following = network.getOrDefault(userId, new HashSet<>());

            while(tweets.size()!=0 && ans.size()!=10){
                Pair<Integer, Integer> curr = tweets.pop();
                if((following.contains(curr.getKey()) || curr.getKey()==userId)
                        && ans.size()!=10) ans.add(curr.getValue());
                store.push(curr);
            }
            while(store.size()!=0) tweets.push(store.pop());
            return ans;
        }

        public void follow(int followerId, int followeeId) {
            Set<Integer> following = network.getOrDefault(followerId, new HashSet<>());
            following.add(followeeId);
            network.put(followerId, following);
        }

        public void unfollow(int followerId, int followeeId) {
            Set<Integer> following = network.get(followerId);
            if(following == null) return;
            following.remove(followeeId);
            network.put(followerId, following);
        }
    }


    // V1_1
    // https://leetcode.com/problems/design-twitter/solutions/3869194/beats-100-8ms-java/
    class Twitter_1_1 {

        ArrayList<Tweet> tweets;
        HashMap<Integer, User> users;

        public Twitter_1_1() {
            tweets = new ArrayList<>();
            users = new HashMap<>();
        }

        public void postTweet(int userId, int tweetId) {
            if(!users.containsKey(userId))
                users.put(userId, new User(userId));
            tweets.add(new Tweet(tweetId, userId));
        }

        public List<Integer> getNewsFeed(int userId) {
            if(!users.containsKey(userId))
                users.put(userId, new User(userId));
            List<Integer> ans = new ArrayList<Integer>();
            int i = tweets.size()-1;
            while(ans.size()<10 && i>=0) {
                if(tweets.get(i).userId==userId || users.get(userId).follows.contains(tweets.get(i).userId))
                    ans.add(tweets.get(i).tweetId);
                i--;
            }
            return ans;
        }

        public void follow(int followerId, int followeeId) {
            if(!users.containsKey(followerId))
                users.put(followerId, new User(followerId));
            if(!users.containsKey(followeeId))
                users.put(followeeId, new User(followeeId));
            User user = users.get(followerId);
            user.follows.add(followeeId);
        }

        public void unfollow(int followerId, int followeeId) {
            if(!users.containsKey(followerId))
                users.put(followerId, new User(followerId));
            if(!users.containsKey(followeeId))
                users.put(followeeId, new User(followeeId));
            User user = users.get(followerId);
            user.follows.remove(followeeId);
        }
    }

    class Tweet {
        int tweetId;
        int userId;
        Tweet(int t, int u) {
            tweetId = t;
            userId = u;
        }
    }

    class User {
        int userId;
        HashSet<Integer> follows;
        User(int u) {
            userId = u;
            follows = new HashSet<>();
        }
    }

    // V2
    // https://leetcode.com/problems/design-twitter/solutions/3400455/simple-solution-for-beginners-with-step-by-step-explanation/
    class Twitter_3 {

        HashMap<Integer,ArrayList<Pair<Integer,Integer>>> posttweet ; // map<userid, < tweetId, time>>
        HashMap<Integer,Set<Integer>> followers ;
        int time;

        public Twitter_3() {
            posttweet = new HashMap<>();
            followers = new HashMap<>();
            time=0;
        }

        public void postTweet(int userId, int tweetId) {
            Pair<Integer,Integer> pair = new Pair<>(tweetId,time);
            ArrayList temp = posttweet.getOrDefault(userId,new ArrayList<>());
            temp.add(pair);
            posttweet.put(userId,temp);
            time++;
        }

        public List<Integer> getNewsFeed(int userId) {
            List<Integer> list = new ArrayList<>();
            Set<Integer> set = followers.getOrDefault(userId,new HashSet<>());
            set.add(userId);
            list.addAll(set);
            HashMap<Integer,Integer> map = new HashMap<>();
            for(int i : list){
                if(posttweet.get(i)!=null)
                    for(Pair<Integer,Integer> j : posttweet.get(i)){
                        map.put(j.getKey(),j.getValue());
                    }
            }

            PriorityQueue<Map.Entry<Integer,Integer>> pq = new PriorityQueue<>(((x,y)->x.getValue()-y.getValue()));
            pq.addAll(map.entrySet());
            while(pq.size()>10){
                pq.poll();
            }
            List<Integer> ans = new ArrayList<>();
            while(pq.size()!=0){
                ans.add(pq.poll().getKey());
            }Collections.reverse(ans);
            return ans;
        }

        public void follow(int followerId, int followeeId) {
            Set<Integer> set = followers.getOrDefault(followerId, new HashSet<>());
            set.add(followeeId);
            followers.put(followerId,set);
        }

        public void unfollow(int followerId, int followeeId) {
            Set<Integer> set = followers.getOrDefault(followerId, new HashSet<>());
            if(set.contains(followeeId))
                set.remove(followeeId);
            followers.put(followerId,set);
        }
    }

}
