-- List all records in table with exceptions.
SELECT score, name
FROM Second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
