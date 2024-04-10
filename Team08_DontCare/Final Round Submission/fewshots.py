few_shots = [
    {
        'Question' : "show me how much stock is left for shoe",
        'SQLQuery' : "SELECT quantity FROM inventory WHERE product = 'shoe'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "There are 100 shoes left in stock."
    },
    {
        'Question' : "The e-mail ID of lens should be updated to lenskart@gmail.com.",
        'SQLQuery' : "UPDATE supplier SET email = 'lenskart@gmail.com' WHERE name = 'lens'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "updated successfully"
    },
    {
        'Question' : "show me the orders table",
        'SQLQuery' : "SELECT * FROM orders",
        'SQLResult': "Result of the SQL query",
        'Answer' : "displaying the table"
    },
    {
        'Question': "who is the supplier of sunglass",
        'SQLQuery' : "SELECT name FROM supplier WHERE product_name = 'sunglass'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "Lenskart"
    },
    {
        'Question': "what's the email of the one who supplied the socks",
        'SQLQuery' : "SELECT email FROM supplier WHERE product_name = 'socks'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "johnfootware@example.com"
    },
    {
        'Question': "Retrieve all orders with the corresponding product name, supplier name, and delivery address",
        'SQLQuery' : "SELECT * FROM orders o JOIN inventory i ON o.product_id = i.id JOIN supplier s ON i.supplier_id = s.supplier_id",
        'SQLResult': "Result of the SQL query",
        'Answer' : "displaying the results"
    },
    {
        'Question': "Calculate the total cost for each order:",
        'SQLQuery' : "SELECT order_id, SUM(cost) FROM order GROUP BY order_id",
        'SQLResult': "Result of the SQL query",
        'Answer' : "order 3 with total cost of 45000, order 1 with total cost of 44500,order 2 with total cost of 40500"
    },
    {
        'Question': "Retrieve orders that haven't been received yet along with their delivery address and product details:",
        'SQLQuery' : "SELECT * FROM orders o JOIN inventory i ON o.product_id = i.id WHERE o.status = 'Sent'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "shirt from newyork"
    },
    {
        'Question': "At what time was the product name was delivered to us",
        'SQLQuery' : "SELECT received FROM supplier WHERE product_name = 'Product Name'",
        'SQLResult': "Result of the SQL query",
        'Answer' : " march 20 2024 and march 14 2024"
    },
    {
        'Question': "what products are delivered by the John Footware to us",
        'SQLQuery' : "SELECT product_name FROM supplier WHERE name = 'John Footware'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "shoes,socks"
    },
    {
        'Question': "Update email of Bombay clothing to cty.gmail.com",
        'SQLQuery' : "UPDATE supplier SET email = 'cty.gmail.com' WHERE name = 'Bombay clothing'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "updated succesfully"
    },
    {
        'Question': "add new supplier whose name is kitex and id is 67890 and Product id is 12455 and product name is undergarments and email as supplier@email.com phone number as 89909765",
        'SQLQuery' : "INSERT INTO supplier (id, name, address, email, phone, product_id, product_name, quantity, sent, received, cost, status, supplier_id) VALUES (67890, 'kitex', 'new delhi', 'supplier@email.com', 89909765, 12455, 'undergarments', 100, CURDATE(), CURDATE(), 10000, 'arrived', 1)",
        'SQLResult': "Result of the SQL query",
        'Answer' : "updated succesfully"
    },
    {
        'Question': "delete supplier with id 67890",
        'SQLQuery' : "DELETE FROM supplier WHERE supplier_id = 67890",
        'SQLResult': "Result of the SQL query",
        'Answer' : "updated succesfully"
    },
    {
        'Question' : "how many units of socks do we have?",
        'SQLQuery' : "SELECT SUM(quantity) FROM inventory WHERE product LIKE '%sock%'",
        'SQLResult': "Result of the SQL query",
        'Answer' : "We currently have a total of 250 pairs of socks available."
    },
    {
        'Question' : "do transactiion",
        'SQLQuery' : """
                     BEGIN;
                         UPDATE inventory SET quantity = quantity - 30 WHERE product = 'shirt';
                         IF @@ROWCOUNT =  0 THEN ROLLBACK; ELSE COMMIT; END IF;
                     """,
        'SQLResult': "Transaction was successful.",
        'Answer' : "The transaction has been completed. The number of shirts remaining in stock after this transaction is 70."
    },
    {
        'Question' : "rollback  transaction",
        'SQLQuery' : "ROLLBACK",
        'SQLResult': "Transaction rolled back.",
        'Answer' : "Transaction rolled back"
    },
    {
        'Question' : "create table product with product id , product_name and price", 
        'SQLQuery' : """CREATE TABLE product (
                          product_id INT PRIMARY KEY,
                          product_name VARCHAR(40),
                          price DECIMAL(8,2)
                      );""",
        'SQLResult': "",
        'Answer' : "Table created successfully."
    },
    {
        'Question' : "insert values into product table with product id 1 and 2 ,t-shirt and jeans into product_name and finally its price 19.99 and 59.99  ",
        'SQLQuery' : """INSERT INTO product VALUES
                             (1, 't-shirt', 19.99),
                             (2, 'jeans', 59.99);""",
        'SQLResult': "",
        'Answer' : "Data inserted successfully."
    },
    {
        'Question' : "Commit these entries",
        'SQLQuery' : "COMMIT",
        'SQLResult': "Entries committed.",
        'Answer' : "Committed"
    },
    {
        'Question' : "show me all the tables",
        'SQLQuery' :  "SHOW TABLES;",
        'SQLResult': "Result of the SQL query",
        'Answer' : "product, supplier, inventory, order"
    },
    {
        'Question' : "show me the details of supplier who delivered the t-shirts on 9/4/22",
        'SQLQuery' : "SELECT name, address, email, phone FROM supplier WHERE received = '09/04/22';",
        'SQLResult': "Result of the SQL query",
        'Answer' : "john, new york, johnnewyork@gmail.com, 202-939-9888"
    },
    {
        'Question' : "Delete all entries of the table product",
        'SQLQuery' : "TRUNCATE TABLE product;",
        'SQLResult': "All data has been deleted from the product table.",
        'Answer' : "Product table is now empty."
    }
]
