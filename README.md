# Café Management CLI

A **hopefully** somewhat simple CLI application to manage and track orders.

## Current Features

- Dynamic menu tree
- CRUD operations for easy data management:

  - Create ✔
  - Read ✔
  - Update ✔
  - Delete ✔

- Data persistence in CSV format

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
a lot less painful that a typical personal project.

The biggest hurdle I encountered was trying to implement the Dependency Inversion Principle to this
project, which I believe I succeeded in for the most part using Composition but falls short in some areas where some classes are more tightly coupled then
I would have prefered.

For data persistance we moved from none at all, to TXT files and now to CSV. I expect within the week to be working on consolidating knowledge on SQL and
Docker to create a Docker image that connects to a MySQL container to supply our data persistance. This project is already dockerized but will require a
new docker compose file to connect the two images.

All in all this has been a very interesting challenge of following set requirements, and am inspired to try this project in other languages to test my
own knowledge.
