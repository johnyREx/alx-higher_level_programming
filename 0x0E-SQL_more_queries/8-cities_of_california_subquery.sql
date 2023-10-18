-- lists all the cities of California
USE hbtn_0d_usa;
SELECT cities.*
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id
