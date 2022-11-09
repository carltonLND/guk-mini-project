# Café Management CLI

A **hopefully** somewhat simple CLI application to manage and track orders.

## Current Features

- Dynamic menu tree
- Eye catching terminal colors using [Rich](https://github.com/Textualize/rich)
- CRUD operations for easy data management:
  - Create ✔
  - Read ✔

<!-- - Data persistence through .txt files -->

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

docker build .
docker run -it cafe-cli
```

### TODO:

- Fix crash when attempting to load non-existing file
- Refactor data related functionality to their objects
- Create file handler abc class
- Add saving changes when quiting the application
