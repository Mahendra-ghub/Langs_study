use school_db;
create table student(
id int,
name varchar(100));
select * from student;
insert into student(id,name)
values(5,"lucky"),(6,"Mani");
insert into student values(2,"raju"),(4,"naren");
select * from student;
select name from student;
select * from student where id = 4;
alter table student add column contact int;
select * from student;
update student set contact = 9948 where id = 1;
create database Mahi;
drop database Mahi;
delete from student where id=3;
update student set contact = 4830 where id =2; 
select name from student;
insert into student(id,name,contact) values(8,"moni",9967),(9,"lucky",990);
select * from student;

create database Bank;
use Bank;
create table costumer1
(acc_no int primary key, name varchar(100) not null, type varchar(50) not null default 'savings');
select * from costumer1;
insert into costumer1
values(1,"pam","savings");

insert into costumer1(acc_no,name,type) values(1,"ram","savings"),(2,"anju","savings"),(3,"upi","savings"),(4,"lucky","savings"),(5,"sam","savings"),(6,"das","current");

