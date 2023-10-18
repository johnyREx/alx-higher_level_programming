-- lists all the cities of California
USE hbtn_0d_usa;

SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY cities.id;
