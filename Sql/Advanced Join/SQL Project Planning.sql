select start_date, min(end_date)
from
  (select start_date
   from projects
   where start_date not in
       (select end_date
        from projects)) a,
  (select end_date
   from projects
   where end_date not in
       (select start_date
        from projects)) b
where start_date < end_date
group by start_date
order by (min(end_date) - start_date), start_date;