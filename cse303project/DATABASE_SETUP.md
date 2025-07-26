# Database Setup Guide

This project supports both SQLite and MySQL databases. You can easily switch between them using environment variables.

## Current Setup (SQLite - Default)

The project is currently configured to use SQLite by default. No additional setup required.

```bash
python app.py
```

## MySQL Setup with XAMPP

### Step 1: Install XAMPP
1. Download XAMPP from https://www.apachefriends.org/
2. Install and start Apache and MySQL services

### Step 2: Create Database
1. Open phpMyAdmin (http://localhost/phpmyadmin)
2. Create a new database named `cse303_project`
3. Set collation to `utf8mb4_unicode_ci`

### Step 3: Configure Environment Variables

Create a `.env` file in your project root:

```env
# Database Configuration
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cse303_project
DB_USER=root
DB_PASSWORD=
```

### Step 4: Install MySQL Dependencies

```bash
pip install mysql-connector-python PyMySQL
```

### Step 5: Run the Application

```bash
python app.py
```

## MySQL Setup with MySQL Workbench

### Step 1: Install MySQL Server and Workbench
1. Download MySQL Server from https://dev.mysql.com/downloads/mysql/
2. Download MySQL Workbench from https://dev.mysql.com/downloads/workbench/

### Step 2: Create Database
1. Open MySQL Workbench
2. Connect to your local MySQL server
3. Create a new schema named `cse303_project`

### Step 3: Configure Environment Variables

Same as XAMPP setup above, but adjust the password:

```env
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cse303_project
DB_USER=root
DB_PASSWORD=your_mysql_password
```

## Switching Between Databases

### To use SQLite (default):
```env
DB_TYPE=sqlite
```

### To use MySQL:
```env
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cse303_project
DB_USER=root
DB_PASSWORD=your_password
```

## Testing Database Connection

You can test your database connection:

```python
from database import test_connection, init_database

# Test connection
if test_connection():
    print("Database connection successful!")
    # Initialize tables
    if init_database():
        print("Database initialized successfully!")
else:
    print("Database connection failed!")
```

## Key Differences Handled

The code automatically handles these differences between SQLite and MySQL:

1. **Connection**: Different connection methods and parameters
2. **Data Types**:
   - SQLite: `INTEGER`, `TEXT`, `TIMESTAMP`
   - MySQL: `INT`, `VARCHAR`, `TEXT`, `TIMESTAMP`
3. **Auto Increment**:
   - SQLite: `AUTOINCREMENT`
   - MySQL: `AUTO_INCREMENT`
4. **Parameter Placeholders**:
   - SQLite: `?`
   - MySQL: `%s`
5. **Table Engines**: MySQL uses InnoDB for foreign key support

## Troubleshooting

### Common MySQL Issues:

1. **Connection Refused**: Make sure MySQL service is running
2. **Access Denied**: Check username/password in .env file
3. **Database Not Found**: Create the database first in phpMyAdmin/Workbench
4. **Character Set Issues**: Database should use utf8mb4_unicode_ci collation

### Common SQLite Issues:

1. **File Permissions**: Make sure the directory is writable
2. **Database Locked**: Close any other connections to the database file

## Migration Between Databases

If you need to migrate data from SQLite to MySQL or vice versa:

1. Export data from current database
2. Change DB_TYPE in environment
3. Run `init_database()` to create tables
4. Import data to new database

The table structures are compatible between both database types.
