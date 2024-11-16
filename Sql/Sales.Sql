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


