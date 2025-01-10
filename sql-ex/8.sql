select maker 
from Product
where type in ('PC')
except
select maker 
from Product
where type in ('Laptop')
group by maker
;