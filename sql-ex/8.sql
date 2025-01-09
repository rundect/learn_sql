select maker 
from Product
join PC 
on Product.model = PC.model
where PC.speed >= 450
group by maker
;