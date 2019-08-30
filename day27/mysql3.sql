--外连接
	--内连接
	--左外连接left  (outer) join ***  on  
	--有外链接right (outer) join ***  on 
	--全外连接full  (outer) join ***  on 

select salary 
from t_emp
where salary > 1000
order by id
limit 5;


-- 查询入职时间早于其领导的员工。
select e.id ,e.first_name ,e.start_date,m.id,m.first_name,m.start_date
from t_emp e , t_emp m
where e.manager_id = m.id and e.start_date < m.start_date;


--查询每个客户对应的销售。
select c.name ,e.first_name
from t_customer c ,t_emp e
where c.sales_rep_id = e.id;
--对应的左外连接
select c.name ,e.first_name
from t_customer c
left join t_emp e
on c.sales_rep_id = e.id;

-- 查询每个部门名以及对应的区域名。
select d.name ,r.name 
from t_dept d
left join t_region r
on d.region_id = r.id;

-- 查询每个员工的名字，以及对应的领导的名字。
select e.id ,e.first_name ,l.id ,l.first_name 
from t_emp e 
left join t_emp l
on e.manager_id = l.id;

-- 组函数
--求所有员工的总薪资，平均薪资。
select sum(salary) 总薪资,avg(salary) 平均薪资 from t_emp;

--求41号部门的总薪资，平均薪资，最高薪资，最低薪资
select dept_id ,sum(salary) 总薪资,avg(salary) 平均薪资,max(salary) 最高薪资,min(salary) 最低薪资
from t_emp
where dept_id = 41;

--统计1号区域有多少个部门
select  count(*)
from t_dept
where region_id = 1;

--统计所有职位包含sal(不区分大小写)的员工的平均薪资。
select avg(salary)
from t_emp
where lower(title) like '%sal%';

--统计1号区域员工的平均薪资，人数。
select e.id ,avg(e.salary) 平均薪资,count(*) 人数
from t_emp e,t_dept d
where d .region_id = 1 and e.dept_id = d .id ;

--select ...
--from ...
--where ...
--group by ...
--having ...
--order by ..
--limit ..

-- 统计每个部门的人数
select dept_id,count(*),group_concat(first_name)
from t_emp
group by dept_id;

-- 统计每个销售人员对应的客户数量。
select sales_rep_id 销售人员id ,count(*) 客户数量
from t_customer
where sales_rep_id is not null
group by sales_rep_id;

select ifnull(sales_rep_id,"没有销售人员") 销售人员id ,count(*) 客户数量
from t_customer
group by sales_rep_id;

-- 统计每个区域的部门的数量。
select region_id,count(1)
from t_dept
group by region_id; 

-- 统计1号区域每个部门的人数。
select e.dept_id ,count(1)
from t_emp e,t_dept d
where d.region_id  = 1 and e.dept_id = d.id
group by e.dept_id;

-- 统计每个区域员工的数量，平均薪资。
select e.dept_id , count(e.id),avg(salary)
from t_emp e,t_dept d,t_region r
where e.dept_id = d.id and d.region_id = r.id
group by e.dept_id;

-- 统计每个部门每个职位的人数。
select dept_id,title,count(id)
from t_emp
group by dept_id,title;

-- 统计每个部门的人数,显示部门编号，部门名，部门人数。
select e.dept_id,d.name,count(e.id)
from t_emp e,t_dept d
where e.dept_id = d.id
group by e.dept_id,d.name;

-- 查询出部门人数在2人及2人以上的部门编号，人数，平均薪资。
select dept_id ,count(id),avg(salary)
from t_emp
group by dept_id
having count(id) >= 2;

-- 查询部门平均薪资高于1000的部门编号，部门平均薪资。
select dept_id,avg(salary)
from t_emp
group by dept_id
having avg(salary) > 1000;

-- 查询出每个员工薪资都高于1000的部门编号，部门平均薪资，人数。
select dept_id,avg(salary),count(id)
from t_emp
group by dept_id
having min(salary) > 1000 ;

-- 查询出部门编号高于40的部门平均薪资，人数。
select dept_id,avg(salary),count(id)
from t_emp
where dept_id > 40
group by dept_id;

-- 子查询
-- 查询薪资高于Ben(first_name)的员工。
select id ,first_name,last_name,salary
from t_emp
where salary > (
	select salary
	from t_emp
	where first_name = 'Ben'
);

-- 查询高于平均薪资的员工信息。
select id , first_name , last_name , salary
from t_emp
where salary >(select avg(salary) from t_emp);

-- 查询Elena(first_name)所在部门所有员工的平均薪资。
select dept_id,avg(salary)
from t_emp
where dept_id=(
	select dept_id from t_emp where first_name = 'Elena'
)
group by dept_id;

-- 查询1号区域所有员工的平均薪资(通过子查询来完成)。
select avg(salary)
from t_emp
where dept_id in (select id from t_dept where region_id = 1);

-- 查找和Elena一个部门和一样职称(title)的所有员工。
select id,dept_id,title
from t_emp
where (dept_id,title) = (
	select dept_id,title
	from t_emp
	where first_name = 'Elena'
);

-- 查询不是老板的员工
select id ,first_name,last_name
from t_emp
where id not in (
	select manager_id
	from t_emp
	where manager_id is not null
);

-- having子查询
-- 查询人数高于44号部门人数的部门编号，部门人数。
select dept_id,count(id)
from t_emp
group by dept_id
having count(id) > (
	select count(id)
	from t_emp
	where dept_id = 44
);

-- 查询部门平均薪资高于公司平均薪资的部门编号，部门平均薪资。
select dept_id , avg(salary)
from t_emp
group by dept_id
having avg(salary)>(
	select avg(salary)
	from t_emp
);

-- 查询部门平均薪资高于公司平均薪资的部门编号，部门名，部门平均薪资。
select e.dept_id,d.name,avg(salary)
from (
	select dept_id , avg(salary)
	from t_emp
	group by dept_id
	having avg(salary)>(
	select avg(salary)
	from t_emp
	)
) e,t_dept d
where e.dept_id = d.id;

--相关子查询
--查询员工薪资大于1000的所有员工编号，名字，薪资，部门编号，部门名字，并按薪资降序排序。
select id ,first_name ,salary ,dept_id,(
	select name from t_dept d where d.id = dept_id
) dname
from t_emp
where salary > 1000
order by salary desc;

--查询员工：薪资高于同样职称(title)的员工的平均薪资,
--查询结果包含员工id，名字，职称和薪资，并按职称降序排列。
select id , first_name ,title ,salary
from t_emp e
where salary > (
	select avg(salary)
	from t_emp
	where title = e.title
)
order by title DESC;

-- exists 子句
select id ,first_name
from t_emp
where exists(
	select * 
	from t_emp
	where dept_id = 10
);

update t_emp set salary = 3000 where id = 3;

--Mysql的事物特性 ACID
--A:Atomic 原子性 不可分割
--C:Consistency 一致性
--I:Isolation 隔离性
--D:Durability 持久性


create table t_ttest(
     id int(7) auto_increment,
     name varchar(25),
     balance int(7),
     primary key(id)
     );

insert into t_ttest
(name,balance)
values
('zw',1000),
('jzy',1000);

--READ uncomitted --最低的等级
--可以读到其他事务还没有提交的结果
--后果：赃读

--READ commited
--set session transaction isolation level read commited
-- 只能读到别人已提交的数据，但产生了新问题，不能重复读。
--后果：不能重复读。

--Repeatable read
--set session transaction isolation level Repeatable read
--在一个事务中，可以反复读取一个数据结果。
--带来的问题是：幻读

--Serializable
--事务隔离的最高级别，串行化，只能一个事务接着一个事务来处理。
