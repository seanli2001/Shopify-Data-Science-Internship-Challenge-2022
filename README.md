# Shopify-Data-Science-Internship-Challenge-2022
**Question 1:** Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

a) Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 

b) What metric would you report for this dataset?

c) What is its value?

**Question 2:** For this question you’ll need to use SQL. Follow this link to access the data set required for the challenge. Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

a) How many orders were shipped by Speedy Express in total?

b) What is the last name of the employee with the most orders?

c) What product was ordered the most by customers in Germany?

**Question 2 Answers**


**a)** 

SELECT COUNT (*) FROM ORDERS WHERE SHIPPERID =1

There were 54 orders shipped by Speedy Express

**b)**

with employeeCount as
(SELECT  employees.lastname
, count(*) as orderCount

FROM [Orders]
inner join employees on orders.employeeid=employees.employeeid
group by lastname
order by count(*) desc
)
select lastname from employeeCount limit 1;

Peacock was the employee with the most orders

**c)**

with productCountry as(
SELECT products.productname, customers.country from orders
inner join customers on customers.customerid= orders.customerid
inner join orderdetails on orders.orderid=orderdetails.orderid
inner join products on products.productid=orderdetails.productid
)

select productname, count(*) as orderCount from productCountry
where country ='Germany'
group by productname
order by count(*) desc
limit 1


Gorgonzola Telino was the product ordered most by customers in Germany


