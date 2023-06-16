-- пустые рейсы
select f.flight_id, f.flight_no , f.scheduled_departure, f.departure_airport
from flights f
where f.flight_id not in(
	select bp.flight_id
	from boarding_passes bp
	group by bp.flight_id)
and f.status in('Departed', 'Arrived')
;

-- количество вылетов в день
select f.departure_airport, scheduled_departure::DATE, count(scheduled_departure::DATE)
from flights f
group by f.departure_airport, scheduled_departure::DATE
having count(scheduled_departure::DATE) > 1
;

-- количество посадочных мест в каждом самолете
select s.aircraft_code, count(s.seat_no) as seats_count
from seats s
group by s.aircraft_code
;

-- пустые рейсы c количеством посадочных мест в каждом самолете
select f.flight_id, f.flight_no , f.scheduled_departure, f.departure_airport, s.seats_count
from flights f
join (
	select s.aircraft_code, count(s.seat_no) as seats_count
	from seats s
	group by s.aircraft_code
) as s on s.aircraft_code = f.aircraft_code
where f.flight_id not in(
	select bp.flight_id
	from boarding_passes bp
	group by bp.flight_id)
and f.status in('Departed', 'Arrived')
;

-- количество вылетов в день пустых рейсов
select f.departure_airport as "Код аэропорта",
scheduled_departure::DATE as "Дата вылета",
(count(scheduled_departure::DATE) * f.seats_count) as "Количество пустых мест",
sum((count(scheduled_departure::DATE) * f.seats_count)) OVER (ORDER BY f.departure_airport, scheduled_departure::DATE) AS "Накопительный итог"
from (
	select f.flight_id, f.flight_no , f.scheduled_departure, f.departure_airport, s.seats_count
	from flights f
	join (
		select s.aircraft_code, count(s.seat_no) as seats_count
		from seats s
		group by s.aircraft_code
	) as s on s.aircraft_code = f.aircraft_code
where f.flight_id not in(
	select bp.flight_id
	from boarding_passes bp
	group by bp.flight_id)
and f.status in('Departed', 'Arrived')
) as f
group by f.departure_airport, scheduled_departure::DATE, f.seats_count
having count(scheduled_departure::DATE) > 1
order by f.departure_airport, scheduled_departure::DATE
;

