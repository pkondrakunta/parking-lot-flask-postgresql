# Parking Lot Application

An application built with Python, Flask and PostgreSQL for a database.

## 1. Setting up the project

### 1.1 Creating the PostgreSQL Database and User

I will be creating a database called `flask_db` and a database user called `parking` for my Flask application. Open the SQL shell and create the database:
```
CREATE DATABASE flask_db;
```
Next, I am creating a database user for our project. 
```
CREATE USER parking WITH PASSWORD 'admin';
```
Giving this new user access to administer your new database:
```
GRANT ALL PRIVILEGES ON DATABASE flask_db TO parking;
```

> Note: To confirm the database was created, get the list of databases by typing the command: `\l`

### 1.2 Installing the packages

#### Activate a virtual environment for your project [Optional] 
It is better to create virtual environments and install the packages & dependencies on that. Create a venv folder within your project directory:

```
py -3 -m venv venv
```
Activate your environment using:
```
venv\Scripts\activate
```

#### Installing requirements

All the requirements and dependencies have been collated in the file `requirements.txt`, you can install them using the command:

```
pip install -r requirements.txt
```

> Note: This is a one time setup

## 2. Running the project

### 2.1 Initialising the database

Add your environment variables `DB_USERNAME` and `DB_PASSWORD`

```
$env:DB_USERNAME="parking"
$env:DB_PASSWORD="admin"
```

Initialise the database by running the script:
```
python init_db.py
```

 ### 2.2 Running the flask application

 To run the project, use:

 ```
 flask run
 ```

 With the server running, open this URL using your browser: `http://127.0.0.1:5000/`