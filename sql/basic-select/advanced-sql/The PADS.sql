select concat(name,(concat(concat('(',substr(occupation, 1, 1)), ')'))) from OCCUPATIONS order by name;
select 'There are a total of', count(occupation),
    case 
        when count(occupation) = 1 then lower(occupation)
        when count(occupation) > 1 then concat(lower(occupation),'s.')
        end
from OCCUPATIONS group by occupation order by count(occupation), lower(occupation);  