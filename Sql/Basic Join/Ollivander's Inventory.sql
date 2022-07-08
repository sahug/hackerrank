select w.id, wp.age, w.coins_needed, w.power 
from wands w 
join wands_property wp on (w.code = wp.code) 
where wp.is_evil = 0 
and w.coins_needed = (
    select min(coins_needed) 
    from wands w1 
    join wands_property wp1 
    on (w1.code = wp1.code) 
    where w1.power = w.power 
    and wp1.age = wp.age
) 
order by w.power desc, wp.age desc;