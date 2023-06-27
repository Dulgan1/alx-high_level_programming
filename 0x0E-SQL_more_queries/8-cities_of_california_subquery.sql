-- Gets all cities of state California in database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE NAME = 'California') GROUP BY id ORDER BY id ASC;
