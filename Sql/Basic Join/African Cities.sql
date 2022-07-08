select c.name 
from city c
inner join country ctr
on c.countrycode = ctr.code
where ctr.continent = 'Africa';