-- your query
SELECT DISTINCT ON (email) 
    id,
    email
FROM person