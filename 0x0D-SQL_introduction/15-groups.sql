-- Displays records with same score in second_table and also number of occurence
SELECT score, COUNT(score) AS 'number' FROM second_table GROUP BY score ORDER BY number DESC;
