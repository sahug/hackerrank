select n, case 
            when concat(n, ' ') not in (select concat(p, ' ') from BST) then 'Leaf'
            when p is null then 'Root'
            else 'Inner'
            end
from BST
order by n;
