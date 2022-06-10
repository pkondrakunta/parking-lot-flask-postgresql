# Parking Lot Application

An application built with Python, Flask and PostgreSQL for a database.

## 1. Creating the PostgreSQL Database and User

I will be creating a database called `flask_db` and a database user called `parking` for my Flask application. Open the SQL shell and creating the database:
```
CREATE DATABASE flask_db;
```
Next, I am creating a database user for our project. 
```
CREATE USER parking WITH PASSWORD 'admin';
```
Giving this new user access to administer your new database:

GRANT ALL PRIVILEGES ON DATABASE flask_db TO parking;

> Note: To confirm the database was created, get the list of databases by typing the command: `\l`

## 2. Installing the packages

All the requirements and dependencies have been collated in the file `requirements.txt`, you can install it in a virtual environment for your flask application.

```
pip install -r requirements.txt
```

## 3. Setting up and initialising the database

Add your environment variables `DB_USERNAME` and `DB_PASSWORD`

```$env:DB_USERNAME="parking"
$env:DB_PASSWORD="admin"```