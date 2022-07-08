select hacker_id,
       name,
       sum(a)
from
  (select s.hacker_id,
          h.name,
          max(s.score) a
   from submissions s
   inner join hackers h on h.hacker_id=s.hacker_id
   where s.score!=0
   group by s.hacker_id,
            h.name,
            s.challenge_id)
group by hacker_id,
         name
order by 3 desc, 1;