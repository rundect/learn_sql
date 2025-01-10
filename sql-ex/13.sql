select avg(speed)
from PC
join Product
on Product.model = PC.model
where Product.maker = 'A'
;