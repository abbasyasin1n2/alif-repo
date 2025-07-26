#!/usr/bin/env python3
"""
MySQL Configuration for CSE303 Project
Run this script to set up environment variables for MySQL Workbench
"""

import os

# Set environment variables for MySQL Workbench
os.environ['DB_TYPE'] = 'mysql'
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_PORT'] = '3306'
os.environ['DB_NAME'] = 'cse303_project'
os.environ['DB_USER'] = 'root'
os.environ['DB_PASSWORD'] = '64151052'  # Your MySQL password

print("MySQL environment variables set!")
print("Configuration:")
print(f"  Database Type: {os.environ['DB_TYPE']}")
print(f"  Host: {os.environ['DB_HOST']}")
print(f"  Port: {os.environ['DB_PORT']}")
print(f"  Database: {os.environ['DB_NAME']}")
print(f"  User: {os.environ['DB_USER']}")
print(f"  Password: {'*' * len(os.environ['DB_PASSWORD'])}")

# Test the connection
try:
    from database import test_connection, init_database

    print("\nTesting database connection...")
    if test_connection():
        print("✅ Database connection successful!")

        print("Creating database tables...")
        if init_database():
            print("✅ Database tables created successfully!")
            print("\n🎉 MySQL Workbench setup complete!")
            print("\nNext steps:")
            print("1. Run: python app.py")
            print("2. Open: http://localhost:5000")
        else:
            print("❌ Failed to create database tables")
            print("Make sure the database 'cse303_project' exists in MySQL Workbench")
    else:
        print("❌ Database connection failed!")
        print("\nTroubleshooting:")
        print("1. Make sure MySQL server is running")
        print("2. Create database 'cse303_project' in MySQL Workbench:")
        print("   CREATE DATABASE cse303_project CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        print("3. Check your MySQL password is correct")

except Exception as e:
    print(f"❌ Error: {e}")
    print("Make sure you've installed the MySQL dependencies:")
    print("pip install mysql-connector-python PyMySQL")
