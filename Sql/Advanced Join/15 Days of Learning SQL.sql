with r(submission_date, hacker_id) as
  (select distinct submission_date,
                   hacker_id
   from submissions
   where submission_date = to_date('2016-03-01')
   union all select child.submission_date,
                    child.hacker_id
   from r parent,
        submissions child
   where parent.submission_date + 1 = child.submission_date
     and parent.hacker_id = child.hacker_id),
     total as
  (select submission_date,
          count(distinct hacker_id) as total
   from r
   group by submission_date),
     counter as
  (select submission_date,
          hacker_id,
          count(hacker_id) as n
   from submissions
   group by submission_date,
            hacker_id),
     maxperday as
  (select c.submission_date,
          min(c.hacker_id) as hacker_id
   from counter c
   where c.n =
       (select max(k.n)
        from counter k
        where c.submission_date = k.submission_date)
   group by submission_date)
select total.submission_date,
       total.total,
       hackers.hacker_id,
       hackers.name
from total
join maxperday on total.submission_date = maxperday.submission_date
join hackers on maxperday.hacker_id = hackers.hacker_id
order by total.submission_date;
