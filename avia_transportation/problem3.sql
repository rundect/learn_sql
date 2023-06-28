select array_agg (a.model)
from aircrafts a
where a.aircraft_code in(
	select s.aircraft_code
	from seats s
	group by s.aircraft_code
	having count(distinct s.fare_conditions) < 2
)
