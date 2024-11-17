
show tables;
desc sales;
select * from sales;
select Saledate, Amount, Boxes from sales;
select Saledate, Amount, Boxes, Amount/Boxes from sales;
select Saledate, Amount, Boxes, Amount/Boxes as 'Amount per Boxes' from sales;
select * from sales
where Amount>10000;

select * from sales
where Amount>10000
order by Amount desc;

select * from sales
where GeoID = 'G4'
order by PID, Amount desc;

select * from sales
where Amount>10000 and Saledate>='2022-01-01';

select Amount, saledate from sales
where Amount>10000 and year(saledate) = 2022
order by Amount desc;

select * from sales
where Boxes>0 and boxes<=50
order by Boxes Desc;

select * from sales
where Boxes between 0 and 50
order by Boxes desc;

select Amount, Boxes, Saledate, Weekday(Saledate) as 'Day of week' from sales
where weekday(Saledate) = 4;

select * from people;

select * from people 
where Team = "Yummies" or Team = "Delish";

select * from people
where team in ('Yummies', 'Delish')
order by Salesperson; -- in clause opeartor

select * from people
where Salesperson like 'B%';  -- like opeartor= single B letter in names

select * from people   
where Salesperson like "%B%"; -- in this B letter available in salesperson

-- Categoarial division based on Case statement
Select Saledate, Amount,
          case    when Amount<1000 then 'under 1k'
                  when Amount<5000 then 'under 5k'
                  when Amount<10000 then 'under 10k'
			else 'Above 10k'
            end as 'Amount Category'
from sales;
          
