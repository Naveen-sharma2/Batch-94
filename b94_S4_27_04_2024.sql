use b94;
select * from movies;
-- Exercise - 3
select * from movies where title like "Toy Story%";
select title, director from  movies where director like "John Lassester";
select title, director from  movies where director != "John Lassester";
select * from movies where title like "WALL-_";

-- Example 
select distinct director as Unique_Directors from movies;
select * from movies order by title asc;
select * from movies order by year asc limit 2 offset 10;

-- Exercise - 4
select distinct director from movies order by director asc;
select title, year from movies order by year desc limit 4;
select title from movies order by title asc limit 5;
select title from movies order by title asc limit 5 offset 5;

select * from movie_sales;
-- Exercise - 6
select m1.title, m2.domestic_sales, m2.international_sales from
movies m1 inner join movie_sales m2 on m1.id = m2.movie_id;

select title, domestic_sales, international_sales from 
movies inner join movie_sales on movies.id = movie_sales.movie_id 
where international_sales >  domestic_sales;

SELECT 
    title, rating
FROM
    movies
        INNER JOIN
    movie_sales ON movies.id = movie_sales.movie_id
ORDER BY rating DESC;

-- Exercise - 7
select distinct building from employee;
select * from building_capacity;

select distinct building_name, role from building_capacity
left join employee on building_capacity.building_name = employee.building;

create table emp1 as select * from employee;
select * from emp1;

insert into emp1 values ("Engineer", "Yancy I.", null, 0);
insert into emp1 values ("Artist", "Oliver P.", null, 0);

-- Exercise 8
select name, role from emp1 where building is NULL;

select distinct building_name from building_capacity left join 
emp1 on building_name = building where name is Null;

########## Rest will continue ----------
