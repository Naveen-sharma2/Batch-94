use b94;
show tables;
select * from movies;
select * from movie_sales;

-- Exercise - 9
select m1.title, (domestic_sales + international_sales)/1000000 as Combined_Sales
from movies m1 inner join movie_sales m2 on m1.id = m2.movie_id;

select m1.title, (rating *10) as Percent_rating
from movies m1 inner join movie_sales m2 on m1.id = m2.movie_id;

select title, year from movies where year % 2 = 0;

-- Example 
select movie_id, sum(domestic_sales) as Total_Domestic_Sales 
from movie_sales group by movie_id;

-- Exercise -10
select * from employee;
select max(Years_employed) as Max_time from employee;
SELECT 
    role, AVG(Years_employed) AS Avg_Employment
FROM
    employee
GROUP BY role;

SELECT 
    building, sum(Years_employed) AS Totals_years_worked
FROM
    employee
GROUP BY building;

-- Example 
select * from movies;
select year, avg(Length_Mins) as Avg_Mins 
from movies where year > 2000 group by year having year > 2010;

-- Exercise - 11
select count(role) from employee where role = "Artist";

select role,count(*) as No_of_Employee from employee group by role;

select role, sum(Years_Employed) as Total_years 
from employee group by role having role = "Engineer";

-- Exercise 12 and 13 Home-work
-- Exercise - 14
update movies set director = "John Wick" where id = 2;
select * from movies;

update movies set year = 2000 where id = 3;

UPDATE movies 
SET 
    title = 'Toy Story 8',
    director = 'Bruce Lee'
WHERE
    id = 11;

delete from movies where director = "Andrew Stanton";
drop table building_capacity;

#### Always try to take a back-up of your data

#### create tables --- 
# Views are virtual tables, which holds less space than actutal tables
select * from movie_sales;

create view mov_rating as 
select movie_id, Rating from movie_sales;

use b94;
select * from mov_rating;

#### temporary table
create temporary table temp as select * from emp1;

select * from temp;
select avg(years_employed) as Avh_employment from temp;

select * from emp1;
alter table emp1 drop column building;
alter table emp1 rename to emp2;









