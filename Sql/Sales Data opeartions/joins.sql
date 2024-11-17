use awesome chocolates;
select * from sales;
select * from products;
select * from people;

-- joins in sql
select s.Boxes, s.Amount, s.spid, p.spid, p.Salesperson
from sales s join people p
on s.spid = p.spid;

-- left join
select s.saledate, pr.product, s.amount, s.pid, pr.pid
from sales s left join products pr
on s.pid = pr.pid;

-- multiple joints
select s.saledate, pr.product, s.amount, p.team, g.region
from sales s
join products pr on s.pid = pr.pid
join people p on s.spid = p.spid
where s.amount<500 and p.team= "Delish";
select * from geo;

-- multiple join for gro
select s.saledate, pr.product, s.amount, p.team,  g.region
from sales s 
join products pr on s.pid = pr.pid
join people p on s.spid = p.spid
join geo g on g.GeoID = s.GeoID
where s.amount<500 and p.team="" and g.Geo in ("India","Europe")
order by s.saledate;

