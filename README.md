# Café Management CLI

A **hopefully** somewhat simple CLI application to manage and track orders, products and couriers for a pop-up coffee shop.

## Current Features

- Dynamic menu tree
- CRUD operations for easy data management:

  - Create ✔
  - Read ✔
  - Update ✔
  - Delete ✔

- Data persistence in CSV format

## Extra Branch: cli-frontend

- A redesigned frontend utilizing Typer

## Dependencies

- Python 3.10.7+
- Pip / Conda

# Installation

### MacOS / Linux / Windows

```
git clone https://github.com/carltonlnd/guk-mini-project.git cafe-cli/
cd cafe-cli
```

#### Pip Users:

```
python3 -m venv <env>
source ./<env>/bin/activate
pip install -r requirements.txt
```

#### Conda Users:

```
conda create --name <env> --file requirements.txt
conda activate <env>
```

### Build With Docker:

```
git clone https://github.com/carltonlnd/guk-mini-project.git cafe-cli/
cd cafe-cli

docker build -t cafe-cli .
docker run -it cafe-cli


docker start -i cafe-cli
```

## Goals With This Project

This project is designed around supplied requirements for a pop-up cafe that needs a system to help manage and track order, product and courier information.
As time progressed these requirements were built upon for adding new features. With the help of sufficient testing, refactoring of the code base should be
a lot less painful that a typical personal project. Tests were unfortunately not added until 4 weeks into the project, but have already proven to be a
valuable asset to my development workflow which I will do my utmost to not neglect again.

The biggest hurdle I encountered was trying to implement the Dependency Inversion Principle to this
project, which I believe I succeeded in for the most part using Composition but falls short in some areas where some classes are more tightly coupled then
I would have preferred.

My design philosophy when approaching this project was to design each core feature to be self dependant at a lower level. For example I wanted others
to be able to use my menu/ or db/ modules to create their own cli CRUD application. This is what led me into implementing dependency inversion and using
tools such as pythons ABC module as well as Protocols to define interfaces when composing these mechanisms together. An example of this would be that the
cli menu frontend could be swapped for a traditional cli interface or even a web API without much fuss at all.

For data persistence we moved from none at all, to TXT files and now to CSV. I expect within the week to be working on consolidating knowledge on SQL and
Docker to create a Docker image that connects to a MySQL container to supply our data persistence. This project is already dockerized but will require a
new docker compose file to connect the two images.

All in all this has been a very interesting challenge of following set requirements, and am inspired to try this project in other languages to test my
own knowledge.

### Requirements Week by Week

#### Week 1

As a user I want to:

- create a product and add it to a list
- view all products
- _STRETCH_ update or delete a product
  <br/><br/>
- A product should just be a string containing its name, i.e: "Coke Zero"
- A list of products should be a list of strings , i.e: ["Coke Zero"]

#### Week 2

As a user I want to:

- create a product or order and add it to a list
- view all products or orders
- _STRETCH_ I want to be able to update or delete a product or order
  <br/><br/>
- A product should just be a string containing its name, i.e: "Coke Zero"
- A list of products should be a list of strings, i.e: ["Coke Zero"]
- An order should be a dict, i.e:

```python
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "status": "preparing"
}
```

- A list of orders should be a list of dicts, i.e: [{...}.{...}]

#### Week 3

As a user I want to:

- create a product, courier, or order and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data (products and couriers)
- _STRETCH_ update or delete a product, order, or courier
  <br/><br/>
- A product should just be a string containing its name, i.e: "Coke Zero"
- A list of products should be a list of strings, i.e: ["Coke Zero"]
- A courier should just be a string containing its name, i.e: "John"
- A list of couriers should be a list of strings, i.e: ["John"]
- An order should be a dict, i.e:

```python
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing"
}
```

- A list of orders should be a list of dicts, i.e: [{...}.{...}]
- Data should be persisted to a .txt file on a new line for each courier or product, ie:

```
John
Claire
```

#### Week 4

As a user I want to:

- create a product, courier, or order dictionary and add it to a list
- view all products, couriers, or orders
- update the status of an order
- persist my data
- _STRETCH_ update or delete a product, order, or courier
- _BONUS_ list orders by status or courier
  <br/><br/>
- A product should be a dict, i.e:

```python
{
"name": "Coke Zero",
"price": 0.8 # Float
}
```

- A courier should be a dict, i.e:

```python
{
"name": "Bob",
"phone": "0789887889"
}
```

- An order should be a dict, i.e:

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

- Data should be persisted to a .csv file on a new line for each courier, order, or product, ie:

```csv
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",2,preparing,"1,3,4"
```
