-- Write your query below
-- person and address, combine that shit


-- person id along w first and last name
-- address_id is the primary key
SELECT person.first_name, person.last_name, address.city, address.state FROM person
 LEFT JOIN address ON address.person_id = person.person_id;