
# rank-scores
# https://leetcode.com/problems/rank-scores/description/


/*

Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
For example, given the above Scores table, your query should generate the following report (order by highest score):

+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+

*/

# https://github.com/kamyu104/LeetCode/blob/master/MySQL/rank-scores.sql

# V0
SELECT
s1.Score AS Score,
( SELECT count(DISTINCT s2.Score)
       FROM Scores AS s2 
       WHERE s1.Score < s2.Score)  +1 AS "rank"
FROM Scores AS s1
ORDER BY s1.Score DESC

# V0'
# Time:  O(n^3)
# Space: O(n)
# count how many IDs bigger than current ID's score 
# then using that as new-defined-rank 
SELECT Score,  (SELECT COUNT(DISTINCT(Score)) FROM  Scores b WHERE b.Score > a.Score) + 1 AS Rank
       FROM Scores a
       ORDER by Score DESC

# V0''
# IDEA : DENSE_RANK (ORACLE)
# https://leetcode.com/problems/rank-scores/discuss/218193/DENSE_RANK-SQL-SERVER-604-ms
SELECT s.Score as Score,
DENSE_RANK() OVER (ORDER BY s.Score DESC) as Rank
FROM Scores s

# V1
# https://medium.com/data-science-for-kindergarten/leetcode-mysql-178-rank-scores-b59d89f3f551
# Write your MySQL query statement below
SELECT tb1.Score AS Score, (SELECT count(distinct tb2.Score)
                            FROM Scores AS tb2
                            WHERE tb2.Score > tb1.Score) +1 AS     "Rank"
FROM Scores as tb1
ORDER BY tb1.Score DESC;

# V1'
# Ranks table : re-order score by desc -> rank = rank + 1 
# left join Ranks table (new-defined-rank) to Scores table  
SELECT Ranks.Score, Ranks.Rank FROM Scores LEFT JOIN 
       ( SELECT r.Score, @curRow := @curRow + 1  Rank 
            FROM (SELECT DISTINCT(Score), (SELECT @curRow := 0) 
                      FROM Scores ORDER by Score DESC) r
       ) Ranks 
       ON Scores.Score = Ranks.Score
       ORDER by Score DESC