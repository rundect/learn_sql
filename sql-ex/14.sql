select Classes.class, name, country
from Classes
join Ships
on Classes.class = Ships.class
where Classes.numGuns >= 10
;