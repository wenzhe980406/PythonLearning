--时间的获取
select curdate();--当前日期
select 99*99;
--可以给结果列取别名。
select curdate() as today;		-- 在select中通过as取别名
select curdate() today; 			-- as 可以省略

-- 基本查询练习
--- 1. 查询部门表的所有信息
select * from t_dept;
--- 2. 查询员工的名和姓
select first_name ,last_name from t_emp;
select concat(first_name,'_',last_name) 姓名 from t_emp;
--- 3.  查询每个员工的月薪(salary)，年薪(salary*12)
select salary 月薪,salary*12 年薪 from t_emp; 


--判断空值 ifnull(exp1,exp2)	if exp1是空,则返回exp2。否则返回exp2
select ifnull(manager_id ,'CEO') from  t_emp;
select  round(salary * (1 + ifnull(commission_pct,0)/100),2) 全部薪水 from t_emp;

-- 查询员工的信息，提供员工编号，工号，职位和薪资
select id 员工编号, userid 工号,title 职位, salary 薪资 from t_emp;

--查询部门名字，比较不用distinct和使用distinct两种查询语句不同的结果。
select name 部门名字 from t_dept;

select distinct name 部门名字 from t_dept;

--查询员工的编号，姓名和薪资
select id,concat(first_name,'·', last_name) 姓名,salary from t_emp;

-- 排序
-- 语法：
-- select 列1，列2  ......
-- from 表
-- where 条件
-- order by 字段1[ASC|DESC],字段2[ASC|DESC],.............


--查询每个员工的id ,dept_id,title,按照部门编号降序排序
select id,dept_id,title 
from t_emp
order by dept_id desc ,id desc;

-- 查询每个员工的id，dept_id,title,按照部门编号降序排序，如果部门编号相等，按照职位升序。
select id ,dept_id,title
from t_emp
order by dept_id desc , title asc;

--查询员工的提成，按照提成升序排列，没有提成的都置后。
select commission_pct
from t_emp
order by commission_pct is null,commission_pct;

select commission_pct
from t_emp
order by if(isnull(commission_pct),1,0),commission_pct;

--条件查询
--查询所有薪资高于1000的员工(id,salary)
select id,salary
from t_emp
where salary >1000;

--查询41号部门的所有员工(id,dept_id,salary),按照薪资升序排序
select id, dept_id,salary
from t_emp
where dept_id = 41
order by salary;

--查询薪资在1100到1550之间的所有员工。
select id ,salary
from t_emp
where salary between 1100 and 1550; 

--查询部门编号为41,44,45,50的所有员工。
select id ,dept_id
from  t_emp
where dept_id = 41 or dept_id = 44 or dept_id = 45 or dept_id = 50;

--查询所有没有提成的员工。
select id,commission_pct
from t_emp
where commission_pct is null;

--查找姓Smith的员工。
select last_name,first_name
from t_emp
where last_name = 'Smith';

--查找以字母C开头的员工名。
select last_name,first_name
from t_emp
where first_name like 'c%';

--查找第二个字母是e的员工名
select last_name,first_name
from t_emp
where first_name like '_e%';

--查找长度至少是4的员工名
select last_name,first_name
from t_emp
where first_name like '____%';

--查找所有1991年入职的员工。
select id ,concat(first_name,'·', last_name),start_date
from t_emp
where start_date between '1991-01-01' and '1991-12-31';
--where  start_date like '1991%'
--where year(start_date) = 1991;

--查询在41号或者44号部门,并且薪资高于1000的员工。
select id,dept_id,salary
from t_emp
where salary > 1000 and (dept_id = 41 or dept_id = 44);


---条件表达式
select 
	CASE 1  WHEN 1 THEN 'One'
			WHEN 2 THEN 'Two'
			ELSE 'Three'
	END result;
	
select	
	CASE
		WHEN 1 > 0 THEN 'TRUE'
		ELSE 'FALSE'
	END result;
	
--
--不超过800的，税率为0。
--800 – 900, 税率为0.09。
--900 -  1000，税率为0.20，
--1000 -  1100，税率为0.30，
--1100 – 1200，税率0.40，
--1200 – 1300，税率0.42，
--1300 – 1400，税率0.44，
--其他，税率0.45。

select id ,first_name,last_name,salary, 
	CASE 
		WHEN salary < 800 THEN 0
		WHEN salary < 900 THEN 0.09
		WHEN salary < 1000 THEN 0.20
		WHEN salary < 1100 THEN 0.30
		WHEN salary < 1200 THEN 0.40
		WHEN salary < 1300 THEN 0.42
		WHEN salary < 1400 THEN 0.44
		ELSE 0.45
	END result
from t_emp;


--截取
--mysql中的截取比较简单，用limit关键字
-- limit[started] [number]

-- 查询公司员工id前5个的员工
select id ,last_name,first_name
from t_emp
order by id desc limit 5; 

--多表查询
--笛卡尔积

select e.id,e.first_name,e.last_name,e.salary,d.name
from t_emp e ,t_dept d ;

--利用前面的员工表，部门表，查询每个员工id,部门编号，所在的部门名.
select e.id ,dept_id,d.name
from t_emp e,t_dept d
where e.dept_id = d.id;

--查询每个部门名字，及所在的区域名
select d.name 部门名称,r.name 区域名
from t_dept d ,t_region r
where d.region_id = r.id;

--查询每个客户名，及对应的销售名。
select c.name 客户名,concat(e.last_name,"·",e.first_name) 销售名
from t_emp e ,t_customer c
where c.sales_rep_id = e.id; 

--查询每个员工名，及所在的部门名，及所在的区域名
select concat(e.last_name,"·",e.first_name) 员工名 , d.name 部门名字,r.name 区域名
from t_emp e,t_dept d,t_region r
where e.dept_id = d.id and d.region_id = r.id;

--查询员工编号，员工姓名，员工所在部门编号，员工所在部门名称，部门所在区域编号，区域名称。
select e.id 员工编号, concat(e.last_name,"·",e.first_name) 员工名 ,e.dept_id 员工所在部门编号,
		r.id 部门所在区域编号,r.name 区域名称
from t_emp e ,t_dept d ,t_region r
where e.dept_id = d.id and  d.region_id = r.id ;

--查询每个员工的编号，姓名，以及他的领导的员工编号，姓名。
select e.id 员工编号,concat(e.last_name,"·",e.first_name),
		l.id 员工编号,concat(l.last_name,"·",l.first_name)
from t_emp e,t_emp l
where e.manager_id = l.id;

--查询所有员工的薪资和薪资等级。
	create table t_salgrade(
		losal int(6),
		hisal int(6),
		grade char(1)
	);

	INSERT INTO t_salgrade VALUES(0,999,'D');
	INSERT INTO t_salgrade VALUES(1000,1499,'C');
	INSERT INTO t_salgrade VALUES(1500,1999,'B');
	INSERT INTO t_salgrade VALUES(2000,2500,'A');
	
	--查询所有员工的薪资和薪资等级。
	select e.id ,e.salary 薪资,s.grade 等级
	from t_emp e, t_salgrade s
	where e.salary >= s.losal and e.salary <= s.hisal;
	where e.salary between s.losal and s.hisal

--查看每个员工编号，姓名，部门名称，薪资，薪资等级，他的上级的编号，名称，薪资，薪资等级。
--薪资等级不用ABCD，而是转换成“一级”，“二级”，“三级”，“四级”。
select e.id 员工编号,concat(e.last_name,"·",e.first_name) 员工名,d.name 部门名称,e.salary 薪资 , se.grade 薪资等级 ,
	CASE se.grade
		WHEN  'A' THEN '一级'
		WHEN  'B' THEN '二级'
		WHEN  'C' THEN '三级'
		WHEN  'D' THEN '四级'
	END 员工薪水等级,
	m.id 上级编号,concat(m.last_name,"·",m.first_name) 上级姓名,m.salary 上级薪资 ,sm.grade 上级薪资等级 ,
	CASE sm.grade
		WHEN  'A' THEN '一级'
		WHEN  'B' THEN '二级'
		WHEN  'C' THEN '三级'
		WHEN  'D' THEN '四级'
	END 上级薪水等级
from t_emp e,t_emp m ,t_dept d,t_salgrade se,t_salgrade sm
where   e.manager_id = m.id 
	and e.dept_id = d.id  
	and e.salary between se.losal and se.hisal 
	and m.salary between sm.losal and sm.hisal;
	