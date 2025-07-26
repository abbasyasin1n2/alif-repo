"""
Database utilities for CSE303 DBMS Project
This module contains all database-related functions and operations
Supports both SQLite and MySQL databases
"""

import os
from datetime import datetime
from config import Config

# Database configuration from config file
DB_TYPE = Config.DB_TYPE
DATABASE = Config.SQLITE_DATABASE

if DB_TYPE == 'mysql':
    import mysql.connector
    from mysql.connector import Error

    # MySQL configuration
    DB_CONFIG = {
        'host': Config.DB_HOST,
        'port': Config.DB_PORT,
        'database': Config.DB_NAME,
        'user': Config.DB_USER,
        'password': Config.DB_PASSWORD,
        'charset': 'utf8mb4',
        'collation': 'utf8mb4_unicode_ci'
    }
else:
    import sqlite3

def get_db_connection():
    """Get a database connection with appropriate configuration"""
    if DB_TYPE == 'mysql':
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            return conn
        except Error as e:
            print(f"MySQL connection error: {e}")
            return None
    else:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn

def init_database():
    """Initialize the database with all required tables"""
    conn = get_db_connection()
    if not conn:
        print("Failed to connect to database")
        return False

    try:
        cursor = conn.cursor()

        if DB_TYPE == 'mysql':
            # MySQL table creation
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sample_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    title VARCHAR(255) NOT NULL,
                    description TEXT,
                    status VARCHAR(20) DEFAULT 'active',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS activity_log (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    action VARCHAR(100) NOT NULL,
                    description TEXT,
                    ip_address VARCHAR(45),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            ''')

            # Add indexes for better performance (MySQL syntax)
            try:
                cursor.execute('CREATE INDEX idx_users_username ON users(username)')
            except:
                pass  # Index already exists
            try:
                cursor.execute('CREATE INDEX idx_users_email ON users(email)')
            except:
                pass  # Index already exists
            try:
                cursor.execute('CREATE INDEX idx_sample_data_user_id ON sample_data(user_id)')
            except:
                pass  # Index already exists
            try:
                cursor.execute('CREATE INDEX idx_activity_log_user_id ON activity_log(user_id)')
            except:
                pass  # Index already exists

        else:
            # SQLite table creation (original)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sample_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'active',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS activity_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    action TEXT NOT NULL,
                    description TEXT,
                    ip_address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
                )
            ''')

            # Add indexes for better performance
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_users_username ON users(username)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_sample_data_user_id ON sample_data(user_id)')
            cursor.execute('CREATE INDEX IF NOT EXISTS idx_activity_log_user_id ON activity_log(user_id)')

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Database initialization error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def execute_query(query, params=None, fetch_one=False, fetch_all=False):
    """
    Execute a SQL query with optional parameters

    Args:
        query (str): SQL query to execute
        params (tuple): Parameters for the query
        fetch_one (bool): Whether to fetch one result
        fetch_all (bool): Whether to fetch all results

    Returns:
        Result of the query or None
    """
    conn = get_db_connection()
    if not conn:
        return None

    try:
        cursor = conn.cursor()

        if DB_TYPE == 'mysql':
            cursor.execute(query, params or ())

            if fetch_one:
                result = cursor.fetchone()
                if result:
                    # Convert to dict for consistency
                    columns = [desc[0] for desc in cursor.description]
                    result = dict(zip(columns, result))
            elif fetch_all:
                results = cursor.fetchall()
                if results:
                    # Convert to list of dicts for consistency
                    columns = [desc[0] for desc in cursor.description]
                    result = [dict(zip(columns, row)) for row in results]
                else:
                    result = []
            else:
                result = cursor.rowcount
        else:
            cursor = conn.execute(query, params or ())

            if fetch_one:
                result = cursor.fetchone()
            elif fetch_all:
                result = cursor.fetchall()
            else:
                result = cursor.rowcount

        conn.commit()
        return result

    except Exception as e:
        conn.rollback()
        print(f"Database error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_user_by_id(user_id):
    """Get user by ID"""
    return execute_query(
        'SELECT * FROM users WHERE id = %s' if DB_TYPE == 'mysql' else 'SELECT * FROM users WHERE id = ?',
        (user_id,),
        fetch_one=True
    )

def get_user_by_username(username):
    """Get user by username"""
    return execute_query(
        'SELECT * FROM users WHERE username = %s' if DB_TYPE == 'mysql' else 'SELECT * FROM users WHERE username = ?',
        (username,),
        fetch_one=True
    )

def create_user(username, email, password_hash):
    """Create a new user"""
    return execute_query(
        'INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)' if DB_TYPE == 'mysql'
        else 'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
        (username, email, password_hash)
    )

def log_activity(user_id, action, description=None, ip_address=None):
    """Log user activity"""
    return execute_query(
        'INSERT INTO activity_log (user_id, action, description, ip_address) VALUES (%s, %s, %s, %s)' if DB_TYPE == 'mysql'
        else 'INSERT INTO activity_log (user_id, action, description, ip_address) VALUES (?, ?, ?, ?)',
        (user_id, action, description, ip_address)
    )

def get_user_stats():
    """Get basic user statistics"""
    total_users = execute_query('SELECT COUNT(*) as count FROM users', fetch_one=True)
    total_records = execute_query('SELECT COUNT(*) as count FROM sample_data', fetch_one=True)

    return {
        'total_users': total_users['count'] if total_users else 0,
        'total_records': total_records['count'] if total_records else 0
    }

def get_recent_activity(user_id=None, limit=10):
    """Get recent activity logs"""
    placeholder = '%s' if DB_TYPE == 'mysql' else '?'

    if user_id:
        query = f'''
            SELECT al.*, u.username
            FROM activity_log al
            JOIN users u ON al.user_id = u.id
            WHERE al.user_id = {placeholder}
            ORDER BY al.created_at DESC
            LIMIT {placeholder}
        '''
        params = (user_id, limit)
    else:
        query = f'''
            SELECT al.*, u.username
            FROM activity_log al
            JOIN users u ON al.user_id = u.id
            ORDER BY al.created_at DESC
            LIMIT {placeholder}
        '''
        params = (limit,)

    return execute_query(query, params, fetch_all=True)

def backup_database(backup_path=None):
    """Create a backup of the database"""
    if DB_TYPE == 'mysql':
        print("MySQL backup requires mysqldump utility. Please use XAMPP/phpMyAdmin backup features.")
        return False
    else:
        if not backup_path:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = f'backup_{timestamp}.db'

        try:
            import shutil
            shutil.copy2(DATABASE, backup_path)
            return True
        except Exception as e:
            print(f"Backup failed: {e}")
            return False

def get_table_info(table_name):
    """Get information about a table structure"""
    if DB_TYPE == 'mysql':
        return execute_query(f'DESCRIBE {table_name}', fetch_all=True)
    else:
        return execute_query(f'PRAGMA table_info({table_name})', fetch_all=True)

def get_all_tables():
    """Get list of all tables in the database"""
    if DB_TYPE == 'mysql':
        return execute_query(
            "SELECT table_name as name FROM information_schema.tables WHERE table_schema = %s",
            (DB_CONFIG['database'],),
            fetch_all=True
        )
    else:
        return execute_query(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'",
            fetch_all=True
        )

def test_connection():
    """Test database connection"""
    conn = get_db_connection()
    if conn:
        conn.close()
        return True
    return False
