select ctr.continent, round(avg(c.population)-0.5)
from country ctr
inner join city c
on ctr.code = c.countrycode
group by ctr.continent;