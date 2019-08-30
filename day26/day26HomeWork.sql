-1 
select concat(first_name,',',last_name) Name from t_emp;

-2
select id,concat(first_name,',',last_name) Name,(salary * 12)*(1 + commission_pct/10) annual
from t_emp
where if commission_pct not is null ;

-3
select id,concat(last_name,' ',first_name,',',title) 全名和职位名称
from t_emp;

-4
select id,salary 
from t_emp
where id = 1 or id = 3 or id = 5 or id = 7 or id = 9; 

-5
select id ,first_name,salary
from t_emp
where first_name like '___n_%';

-6
select salary,concat(first_name,',',last_name) ename
from t_emp
where (dept_id =41 or dept_id = 44) and salary < 1000;

-7
select last_name , first_name
from t_emp
where lower(last_name) like'__a%';

-8
select last_name , first_name
from t_emp
where last_name like '%a%' and last_name like '%e%';

-9
select last_name ,start_date 
from t_emp
where start_date like '1992%'
ORDER BY last_name ASC;

-10
select id,name
from t_customer
where sales_rep_id is not null;

-11
select id,date_shipped,total
from t_ord
where date_shipped > '1992-09-01';

-12
select first_name
from t_emp
where lower(first_name) like '%be%';

-13
select e.id,e.first_name,d.name
from t_emp e,t_dept d
where e.dept_id = d.id;

-14 
select e.id,e.first_name,e.salary,d.name
from t_emp e,t_dept d,t_region r
where (e.dept_id = d.id and d.region_id = r.id) and r.id = 1
ORDER BY salary ASC;

-15
select c.name 客户名,r.name 区域名
from t_customer c,t_region r
where c.region_id = 1 and r.id = 1 ;

