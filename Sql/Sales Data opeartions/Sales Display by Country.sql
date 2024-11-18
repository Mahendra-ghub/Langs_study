select * from sales;
select * from geo;

-- find county name and amount >5000 by using joins
select g.geo, sum(s.amount) as "total sum"
from sales s
join geo g on s.geoid = g.geoid
where amount>5000
group by g.Geo
order by sum(s.amount) desc;

-- find only canada sales data
select g.geo, s.amount
from sales s
join geo g on g.geoid = s.geoid
where g.geo = 'canada' and s.amount<1000
order by s.amount;
