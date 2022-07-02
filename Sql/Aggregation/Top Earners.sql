select * from (
select ern, count(employee_id) as cnt
from (select (salary*months) as ern, employee_id from employee)
group by ern
order by cnt desc)
where rownum = 1;