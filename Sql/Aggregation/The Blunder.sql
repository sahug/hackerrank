select ceil(avg(salary) - avg(TO_NUMBER(replace(TO_CHAR(salary), 0, '')))) from EMPLOYEES;