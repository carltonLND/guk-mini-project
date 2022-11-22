# Café Management CLI

A somewhat simple CLI application to manage and track orders, products and couriers for a pop-up coffee shop.

## Current Features

- A traditional frontend utilizing [Typer](https://github.com/tiangolo/typer)
- Data persistence using SQLite3 or CSV file format
- CRUD operations for easy data management:

  - Create ✔
  - Read ✔
  - Update ✔
  - Delete ✔

# Installation

```
git clone https://github.com/carltonlnd/guk-mini-project.git cafe-cli/
cd cafe-cli

python3 -m venv <env>
source ./<env>/bin/activate
pip install -r requirements.txt
```

### Dependencies

- Python 3.10.7+

# Usage

```sh
python3 app.py --help

```

![Help Example](https://i.ibb.co/k667yJK/cafe-help.png)

## Goals With This Project

This CLI app was worked on over the course of 5 weeks with evolving requirements, the final week containing both week 5 and 6.
For this reason I found this project vastly different to working on my own personal projects where time constraints and client
requirements are up to my own discretion.

### Design Choices

My primary goal when approaching this project was to design my software to be modular. As in I could, rather seamlessly, swap out
functionality of the application as required. I originally wanted to have separate frontend interfaces to display this feature
in action, but as the frontend was a lot more time consuming, I opted to approach this by instead swapping out the backend api following
week 5 and 6 requirements.

I used a repository pattern to design the core functionality of this application. I currently have two repositories that are both built from
an abstract base, one for doing CRUD operations on and persisting to a SQLite database, and one for CSV files. Because these repositories are
built off of an abstraction, it means that any frontend that uses the CSV repository, can also swap in the SQLite repository without changing
anything but initializing a different repository. This is demonstrated in the application by using the `--csv` flag to switch to CSV file
format.

### Meeting Requirements & Time Constraints

During the course of this project I was very undecided on what my application would like at the end, and because of this I ended up not just
refactoring code but completely redesigning from the ground up to achieve my design choice. Because of this there is some **STRETCH** and
**BONUS** goals that were not met, despite being relatively simple to implement.

For base requirements my application meets them all except a single change in the final week. Where we went from using a string to represent an
order status, to instead the status' ID as a foreign key to it's own table in the database. To work around this, the order status is stored and
represented still as a string, but instead in the format of `"<id> (<status>)"`.

### Areas To Improve

The biggest pain that I experienced during this project stems, not surprisingly, from my lack of decisiveness and planning early on in the project.
Now while I can say this was made difficult as the requirements evolved weekly, setting on concrete goal earlier than week 4 would have helped
massively. This is especially true when it comes to implementing tests, as my project's design was only finalized much too late I found myself having
to completely scrap tests that were designed off of previous iterations before introducing my implementation of the repository pattern. Currently input
validation for the backend database is almost completely reliant on the frontend validating user input first. Ideally I would like this validation to be
in place for the backend also, as this is where invalid user input can cause the most damage.

### Things I Would Like To Add

Should time allow, I would love to package this project into it's own binary executable and upload it to allow for easy installation and use. One
caveat however is that Python being an interpreted scripting language makes it harder to compile, and as such I need to do some learning on the
topic.

While out of scope for our CLI requirements, I think it would be nice to build a simple web application to further solidify my modular design choice.
This would feature calls to the backend api which would be almost identical to how the CLI app is being used right now. Especially if I opt to create
this backend using [FastAPI](https://github.com/tiangolo/fastapi), as our current frontend uses [Typer](https://github.com/tiangolo/typer) which is
described as "FastAPI's little sibling".

### Requirements For Reference

<details>
<summary>Week 1</summary>
<br>
As a user I want to:
<ul>
<li>create a product and add it to a list</li>
<li>view all products</li>
<li>STRETCH update or delete a product</li>
<br>
<li>A product should just be a string containing its name, i.e: "Coke Zero"</li>
<li>A list of products should be a list of strings , i.e: ["Coke Zero"]</li>
</ul>
</details>
<br>
<details>
<summary>Week 2</summary>
<br>
As a user I want to:
<ul>
<li>create a product or order and add it to a list</li>
<li>view all products or orders</li>
<li>STRETCH I want to be able to update or delete a product or order</li>
<br>
<li>A product should just be a string containing its name, i.e: "Coke Zero"</li>
<li>A list of products should be a list of strings, i.e: ["Coke Zero"]</li>
<li>An order should be a dict, i.e:</li>

```python
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "status": "preparing"
}
```

<li>A list of orders should be a list of dicts, i.e: [{...}.{...}]</li>
</ul>
</details>
<br>
<details>
<summary>Week 3</summary>
<br>
As a user I want to:
<ul>
<li>create a product, courier, or order and add it to a list</li>
<li>view all products, couriers, or orders</li>
<li>update the status of an order</li>
<li>persist my data (products and couriers)</li>
<li>STRETCH update or delete a product, order, or courier</li>
<br>
<li>A product should just be a string containing its name, i.e: "Coke Zero"</li>
<li>A list of products should be a list of strings, i.e: ["Coke Zero"]</li>
<li>A courier should just be a string containing its name, i.e: "John"</li>
<li>A list of couriers should be a list of strings, i.e: ["John"]</li>
<li>An order should be a dict, i.e:</li>

```python
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing"
}
```

<li>A list of orders should be a list of dicts, i.e: [{...}.{...}]</li>
<li>Data should be persisted to a .txt file on a new line for each courier or product, ie:</li>

```
John
Claire
```

</ul>
</details>
<br>
<details>
<summary>Week 4</summary>
<br>
As a user I want to:
<ul>
<li>create a product, courier, or order dictionary and add it to a list</li>
<li>view all products, couriers, or orders</li>
<li>update the status of an order</li>
<li>persist my data</li>
<li>STRETCH update or delete a product, order, or courier</li>
<li>BONUS list orders by status or courier</li>
<br>
<li>A product should be a dict, i.e:</li>

```python
{
"name": "Coke Zero",
"price": 0.8 # Float
}
```

<li>A courier should be a dict, i.e:</li>

```python
{
"name": "Bob",
"phone": "0789887889"
}
```

<li>An order should be a dict, i.e:</li>

```python
{
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2, # Courier index
"status": "preparing",
"items": "1, 3, 4" # Product index
}
```

<li>Data should be persisted to a .csv file on a new line for each courier, order, or product, ie:</li>

```csv
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",2,preparing,"1,3,4"
```

</ul>
</details>
<br>
<details>
<summary>Week 5</summary>
<br>
As a user I want to:
<ul>
<li>create a product or courier and add it to a database table</li>
<li>create an order and add the order dictionary to a list</li>
<li>view all products, couriers, or orders</li>
<li>update the status of an order</li>
<li>persist my data</li>
<li>STRETCH update or delete a product, order, or courier</li>
<li>BONUS list orders by status or courier</li>
<li>BONUS track my product inventory</li>
<li>BONUS import/export my entities in CSV format</li>
<br>
<li>A row in the products table should contain the following information:</li>

```python
{
 "id": 4,
 "name": "Coke Zero",
 "price": 0.8
}
```

<li>A row in the couriers table should contain the following information:</li>

```python
{
 "id": 2,
 "name": "Bob",
 "phone": "0789887889"
}
```

<li>An order should be a dict, i.e:</li>

```python
{
 "customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334",
 "courier": 2, # Courier ID
 "status": "preparing",
 "items": "1, 3, 4" # Product IDs
}
```

<li>Orders should be persisted to a .csv file on a new line for each order, ie:</li>

```csv
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",2,preparing,"1,3,4"
```

</ul>
</details>
<br>
<details>
<summary>Week 6</summary>
<br>
As a user I want to:
<ul>
<li>create a product, courier, or order and add it to a table</li>
<li>view all products, couriers, or orders</li>
<li>update the status of an order</li>
<li>persist my data in a database</li>
<li>STRETCH delete or update a product, order, or courier</li>
<li>BONUS display orders by status or courier</li>
<li>BONUS CRUD a list of customers</li>
<li>BONUS track my product inventory</li>
<li>BONUS import/export my entities in CSV format</li>
<br>
<li>A row in the products table should contain the following information:</li>

```python
{
 "id": 4,
 "name": "Coke Zero",
 "price": 0.8
}
```

<li>A row in the couriers table should contain the following information:</li>

```python
{
 "id": 2,
 "name": "Bob",
 "phone": "0789887889"
}
```

<li>A row in the orders table should contain the following information:</li>

```python
{
 "id": 1,
 "customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334",
 "courier": 2, # Courier ID
 "status": 1, # Order status ID
 "items": "1, 3, 4" # Product IDs
}
```

<li>A row in the order_status table should contain the following information:</li>

```python
{
 "id": 1,
 "order_status": "preparing"
}
```
