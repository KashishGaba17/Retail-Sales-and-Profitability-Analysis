CREATE database retail;
use retail;
ALTER USER 'root'@'localhost'
IDENTIFIED WITH mysql_native_password
BY 'Kashdata17@';
FLUSH PRIVILEGES;
select * from invoice limit 10;


select count(*) from invoice;
select min(invoice_date) from invoice;
select count( distinct customer_id) from invoice;
select count( distinct stockcode) from invoice;
select country,count(*) as total from invoice group by country order by total desc ;

select sum(total_amount) as revenue from invoice;
select sum(total_amount) as revenue,country from invoice group by country order by revenue desc limit 10;
select sum(total_amount) as revenue ,month from invoice group by month;
select description,sum(total_amount) as revenue from invoice  group by description order by revenue desc limit 10;
select avg(tot) as aov from (select invoice,sum(total_amount) as tot from invoice group by invoice)t;
select sum(total_amount) as tot,invoice from invoice group by invoice order by tot desc limit 10;
select avg(ipo) from (select invoice,sum(quantity) as ipo from invoice group by invoice) t;

select customer_type,count(*) as customer_count from 
( select customer_id, case when count(distinct invoice)=1 then "one-time" else "repeat" end as customer_type from invoice group by customer_id)t
group by customer_type;

select customer_id,sum(total_amount) as revenue from invoice where customer_id is not null group by customer_id order by revenue desc limit 10;

select avg(customer_revenue) from(select customer_id,sum(total_amount) as customer_revenue from invoice where customer_id is not null group by customer_id)t;

select customer_id,count(invoice) as tot from invoice where customer_id is not null group by customer_id order by tot desc limit 10 ;


