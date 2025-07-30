
from .connection import get_db_connection, DB_TYPE
from .user_queries import execute_query
from datetime import datetime
from ..config.config import Config

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
                CREATE TABLE IF NOT EXISTS suppliers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    contact_person VARCHAR(100),
                    phone VARCHAR(20),
                    email VARCHAR(100),
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    animal_type VARCHAR(50),
                    cut_type VARCHAR(50),
                    processing_date DATE,
                    storage_requirements VARCHAR(255),
                    shelf_life INT,
                    packaging_details VARCHAR(255),
                    supplier_id INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE SET NULL
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inventory_batches (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    product_id INT NOT NULL,
                    batch_number VARCHAR(100),
                    quantity DECIMAL(10, 2) NOT NULL,
                    arrival_date DATE,
                    expiration_date DATE,
                    storage_location VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
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

        else:
            # SQLite table creation
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
                CREATE TABLE IF NOT EXISTS suppliers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    contact_person TEXT,
                    phone TEXT,
                    email TEXT,
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    animal_type TEXT,
                    cut_type TEXT,
                    processing_date DATE,
                    storage_requirements TEXT,
                    shelf_life INTEGER,
                    packaging_details TEXT,
                    supplier_id INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE SET NULL
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inventory_batches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER NOT NULL,
                    batch_number TEXT,
                    quantity REAL NOT NULL,
                    arrival_date DATE,
                    expiration_date DATE,
                    storage_location TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
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

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Database initialization error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def test_connection():
    """Test database connection"""
    conn = get_db_connection()
    if conn:
        conn.close()
        return True
    return False

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
            shutil.copy2(Config.SQLITE_DATABASE, backup_path)
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
