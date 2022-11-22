# Café Management CLI

A **hopefully** somewhat simple CLI application to manage and track orders, products and couriers for a pop-up coffee shop.

## Current Features

- Dynamic menu tree
- CRUD operations for easy data management:
- A traditional frontend utilizing [Typer](https://github.com/tiangolo/typer)

  - Create ✔
  - Read ✔
  - Update ✔
  - Delete ✔

- Data persistence in CSV format

## Dependencies

- Python 3.10.7+

# Installation

```
git clone https://github.com/carltonlnd/guk-mini-project.git cafe-cli/
cd cafe-cli

python3 -m venv <env>
source ./<env>/bin/activate
pip install -r requirements.txt
```

# Usage

```sh
python3 app.py --help

```

![Help Example](https://i.ibb.co/k667yJK/cafe-help.png)

## Goals With This Project

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
