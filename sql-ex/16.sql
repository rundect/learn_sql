select distinct A.model, B.model, A.speed, A.ram
from PC as A, PC as B
where A.speed = B.speed and A.ram = B.ram and A.model > B.model
;