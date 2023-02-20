-- Displays alll cities in hbtn_0d_usa
-- in format, cities.id cities.name state.name

SELECT cities.id, cities.name, states.name FROM cities JOIN  states WHERE cities.state_id = states.id ORDER BY cities.id ASC;
