with thousand as
  (select *
   from
     (select level lvl
      from dual connect by level <= 1000)
   where lvl > 1)
select listagg(t1.lvl, '&') within group(order by t1.lvl)
from thousand t1
where t1.lvl <=
    (select count(distinct t2.lvl) + 2
     from thousand t2
     where t2.lvl < t1.lvl
       and mod(t1.lvl, t2.lvl) > 0);