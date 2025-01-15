select distinct Product.type, Laptop.model, Laptop.speed
from PC, Laptop
join Product
on Product.model = Laptop.model
where Laptop.speed < all(
    select PC.speed
    from PC
)
;