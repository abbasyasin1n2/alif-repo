#!/usr/bin/env python3
"""
Environment Setup Helper for CSE303 Project
This script helps you configure environment variables for database setup
"""

import os

def create_env_file():
    """Create a .env file with database configuration"""

    print("=== CSE303 Project Database Setup ===\n")

    print("Choose your database type:")
    print("1. SQLite (Default - No additional setup required)")
    print("2. MySQL (Requires XAMPP or MySQL Workbench)")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    env_content = []

    if choice == "2":
        print("\n=== MySQL Configuration ===")

        host = input("Database Host (default: localhost): ").strip() or "localhost"
        port = input("Database Port (default: 3306): ").strip() or "3306"
        database = input("Database Name (default: cse303_project): ").strip() or "cse303_project"
        user = input("Database User (default: root): ").strip() or "root"
        password = input("Database Password (leave empty if none): ").strip()

        env_content = [
            "# Database Configuration",
            "DB_TYPE=mysql",
            f"DB_HOST={host}",
            f"DB_PORT={port}",
            f"DB_NAME={database}",
            f"DB_USER={user}",
            f"DB_PASSWORD={password}",
            "",
            "# Flask Configuration",
            "FLASK_ENV=development",
            "SECRET_KEY=your-secret-key-change-this-in-production"
        ]

        print(f"\n✓ MySQL configuration created!")
        print(f"✓ Make sure to create database '{database}' in phpMyAdmin or MySQL Workbench")

    else:
        env_content = [
            "# Database Configuration",
            "DB_TYPE=sqlite",
            "",
            "# Flask Configuration",
            "FLASK_ENV=development",
            "SECRET_KEY=your-secret-key-change-this-in-production"
        ]

        print("\n✓ SQLite configuration created!")

    # Write .env file
    with open('.env', 'w') as f:
        f.write('\n'.join(env_content))

    print(f"✓ Environment file created: .env")

    return choice == "2"

def install_dependencies(mysql_setup=False):
    """Install required dependencies"""

    print("\n=== Installing Dependencies ===")

    if mysql_setup:
        print("Installing MySQL dependencies...")
        os.system("pip install mysql-connector-python PyMySQL")

    print("Installing Flask dependencies...")
    os.system("pip install -r requirements.txt")

    print("✓ Dependencies installed!")

def test_setup():
    """Test the database setup"""

    print("\n=== Testing Database Setup ===")

    try:
        from database import test_connection, init_database

        if test_connection():
            print("✓ Database connection successful!")

            if init_database():
                print("✓ Database tables created successfully!")
                return True
            else:
                print("✗ Failed to create database tables")
                return False
        else:
            print("✗ Database connection failed!")
            return False

    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("Make sure all dependencies are installed")
        return False
    except Exception as e:
        print(f"✗ Setup error: {e}")
        return False

def main():
    """Main setup function"""

    print("Welcome to CSE303 Project Database Setup!\n")

    # Create environment configuration
    mysql_setup = create_env_file()

    # Install dependencies
    install_dependencies(mysql_setup)

    # Test the setup
    if test_setup():
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Run: python app.py")
        print("2. Open: http://localhost:5000")
        print("3. Register a new account and test the application")

        if mysql_setup:
            print("\nMySQL Notes:")
            print("- Make sure XAMPP/MySQL is running")
            print("- Create the database in phpMyAdmin/MySQL Workbench")
            print("- Check DATABASE_SETUP.md for detailed instructions")
    else:
        print("\n❌ Setup failed!")
        print("Please check the error messages above and try again.")
        print("See DATABASE_SETUP.md for troubleshooting help.")

if __name__ == "__main__":
    main()
