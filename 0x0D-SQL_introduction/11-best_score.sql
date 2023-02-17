-- Displays in order of scores and from score to name, the records that have 
-- score greater or equal to 10.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
