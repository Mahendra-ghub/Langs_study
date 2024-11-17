-- group by using sql
select * from geo;
select *from sales;
select * from people;
select * from products;
select Geoid, sum(Amount)
from sales
group by geoid
order by sum(Amount);

select g.geo, sum(amount), Avg(amount), sum(boxes)
from sales s
join geo g on s.geoid = g.geoid
group by g.geo;

select p.team, pr.category,sum(amount), sum(boxes)
from sales s
join people p on s.spid = p.spid
join products pr on s.pid = pr.pid
where p.team !=""
group by pr.category, p.team
order by pr.category, p.team;
 
 -- products and total amount
 select pr.product, sum(s.amount) as 'Total amount'
 from sales s
 join products pr on pr.pid = s.pid
 group by pr.product
 order by 'Total amount' desc
 limit 10; -- limit operator limit untill the 10 values