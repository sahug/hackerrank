SELECT DISTINCT(CITY) FROM STATIOn WHERE NOT REGEXP_LIKE(CITY, '^[AEIOU]', 'i');