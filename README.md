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

**Question 1 Answers**

**a)**


Their calculation is giving an average order amount of 3145.13, which appears to be a bit high for the average cost of a sneaker. We can begin by doing some analysis on the dataset to gauge how they are getting this value. 

By opening up the excel file and clicking on the column "order amount" we can observe in the bottom right that the average in this column is 3145.13, alternatively we can use excel code to get this result: 

```
=AVERAGE(D:D)
```

Each value in the order amount, is also tied to a number of items ordered by the consumer. Now I know that their answers were based off giving the average of the order amount column which is a miscalculation on finding average cost for a shoe. 


**b)** 

A better metric to report would be giving an average based on the total order amount, divided by the quantity of items ordered.

**c)**

To solve this we can use Python:

```
import pandas as pd

df = pd.read_excel('questionOneData.xlsx')
total= df["total_items"].sum()
df= df["order_amount"]
print(df.sum()/total)
```
Out:
```
357.92152221412965
```
Therefore the correct value for the average cost of a shoe would be 357.92, which is a lot better than the initial calculation of 3145.13, and this is inline with how the sneakers are a relatively affordable product.


**Question 2 Answers**


**a)** 
```
SELECT COUNT (*) FROM ORDERS WHERE SHIPPERID =1
```
There were 54 orders shipped by Speedy Express

**b)**
```
with employeeCount as
(SELECT  employees.lastname
, count(*) as orderCount

FROM [Orders]
inner join employees on orders.employeeid=employees.employeeid
group by lastname
order by count(*) desc
)
select lastname from employeeCount limit 1;
```
Peacock was the employee with the most orders

**c)**

There were two ways of interpreting the question c, I have included both below.

```with productCountry as(
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

```
Gorgonzola Telino was the product ordered most by customers in Germany

Whereas, 

```
SELECT SUM(Quantity) AS [Volume Sold], ProductName FROM OrderDetails
INNER JOIN Products ON OrderDetails.ProductID = Products.ProductID
WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID IN (SELECT CustomerID FROM Customers WHERE Country='Germany'))
GROUP BY ProductName
ORDER BY SUM(Quantity) DESC;
```

Boston Crab meat was the product ordered most quantity wise, by customers in 
Germany, with a volume of 160 sold.


