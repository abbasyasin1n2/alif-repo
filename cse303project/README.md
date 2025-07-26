# CSE303 Database Management System Project

A comprehensive database management application built with Flask, Bootstrap, and support for both SQLite and MySQL databases for the CSE303 Database Management course.

## 🚀 Features

- **Multi-Database Support**: Works with both SQLite and MySQL databases
- **User Authentication**: Secure registration and login system using Flask-Login
- **Manual SQL Operations**: Direct SQL queries without ORM for better understanding
- **Modern UI**: Responsive design with Bootstrap 5
- **Database Management**: Complete CRUD operations with configurable database backend
- **Activity Logging**: Track user actions and system activities
- **Dashboard**: Interactive dashboard with statistics and quick actions
- **Easy Setup**: Automated setup script for database configuration

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: Bootstrap 5 + HTML/CSS/JavaScript
- **Database**: SQLite or MySQL (configurable)
- **Authentication**: Flask-Login
- **Styling**: Bootstrap 5 + Custom CSS

## 📁 Project Structure

```
cse303project/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── database.py           # Database utilities (SQLite + MySQL support)
├── setup_env.py          # Environment setup helper script
├── DATABASE_SETUP.md     # Detailed database setup guide
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── templates/           # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Home page
│   ├── dashboard.html   # User dashboard
│   └── auth/           # Authentication templates
│       ├── login.html   # Login page
│       └── register.html # Registration page
└── static/             # Static files
    ├── css/
    │   └── custom.css   # Custom styles
    ├── js/
    │   └── main.js      # JavaScript functionality
    └── images/          # Image assets
```

## 🔧 Quick Setup

### Option 1: Automated Setup (Recommended)

1. **Run the setup script**

   ```bash
   python setup_env.py
   ```

2. **Follow the prompts** to configure your database (SQLite or MySQL)

3. **Start the application**

   ```bash
   python app.py
   ```

### Option 2: Manual Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Choose your database setup:**

   **For SQLite (Default):**

   ```bash
   # No additional setup required
   python app.py
   ```

   **For MySQL (XAMPP/MySQL Workbench):**

   ```bash
   # Install MySQL dependencies
   pip install mysql-connector-python PyMySQL

   # Create .env file with MySQL configuration
   # See DATABASE_SETUP.md for detailed instructions
   ```

3. **Access the application**
   - Open your web browser
   - Navigate to `http://localhost:5000`

## 🗄️ Database Configuration

### SQLite (Default)

- No additional setup required
- Database file created automatically
- Perfect for development and testing

### MySQL (XAMPP/MySQL Workbench)

- Requires XAMPP or MySQL Workbench installation
- Create database named `cse303_project`
- Configure connection in `.env` file

**Environment Variables (.env file):**

```env
# For SQLite
DB_TYPE=sqlite

# For MySQL
DB_TYPE=mysql
DB_HOST=localhost
DB_PORT=3306
DB_NAME=cse303_project
DB_USER=root
DB_PASSWORD=your_password
```

See `DATABASE_SETUP.md` for detailed setup instructions.

## 📊 Database Schema

The application automatically creates tables compatible with both SQLite and MySQL:

### Users Table

```sql
-- SQLite version
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MySQL version
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

### Sample Data Table

```sql
-- Automatically adapts to your chosen database type
CREATE TABLE sample_data (
    id [AUTO_INCREMENT_TYPE] PRIMARY KEY,
    user_id [INT_TYPE],
    title [VARCHAR/TEXT] NOT NULL,
    description TEXT,
    status [VARCHAR/TEXT] DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);
```

## 🔐 Security Features

- Password hashing using SHA-256
- Session management with Flask-Login
- CSRF protection
- SQL injection prevention with parameterized queries
- Input validation and sanitization
- Database-agnostic query handling

## 🎨 UI Components

- **Responsive Navigation**: Bootstrap navbar with user dropdown
- **Flash Messages**: Alert system for user feedback
- **Forms**: Styled forms with validation
- **Dashboard**: Statistics cards and quick actions
- **Tables**: Custom styled data tables
- **Buttons**: Consistent button styling throughout

## 📝 Usage

### First Time Setup

1. Run `python setup_env.py` for guided setup
2. Choose SQLite (easy) or MySQL (advanced)
3. Follow the configuration prompts

### Registration & Login

1. Navigate to `http://localhost:5000`
2. Register a new account
3. Login and access the dashboard

### Database Testing

- Visit `http://localhost:5000/test-db` to verify database connection
- Check console output for connection status

## 🔧 Customization for Your Project

### Adding New Features

1. **Database**: Add new tables in `database.py` (works with both SQLite and MySQL)
2. **Routes**: Add new routes in `app.py`
3. **Templates**: Create new HTML templates in `templates/`
4. **Styling**: Add custom CSS in `static/css/custom.css`

### Switching Databases

- Change `DB_TYPE` in your `.env` file
- Restart the application
- Tables will be created automatically

## 🐛 Troubleshooting

### Common Issues

1. **Database connection failed**
   - For SQLite: Check file permissions
   - For MySQL: Verify XAMPP/MySQL is running and credentials are correct

2. **Import errors**
   - Run `pip install -r requirements.txt`
   - For MySQL: `pip install mysql-connector-python PyMySQL`

3. **Port already in use**
   - Change port in `app.run()` or stop other applications

4. **MySQL specific issues**
   - Ensure database exists in phpMyAdmin/MySQL Workbench
   - Check username/password in `.env` file
   - Verify MySQL service is running

See `DATABASE_SETUP.md` for detailed troubleshooting.

## 📚 Learning Objectives

This project demonstrates:

- Multi-database application development
- Flask web application development
- Manual SQL query writing for different database systems
- User authentication and session management
- Frontend development with Bootstrap
- Database design and relationships
- Environment-based configuration
- Security best practices in web development

## 🎯 Perfect for CSE303 Projects

This structure is designed to be easily adaptable for various CSE303 project requirements:

- ✅ **Manual SQL**: No ORM, direct SQL queries as required
- ✅ **MySQL Support**: Works with XAMPP and MySQL Workbench
- ✅ **Extensible**: Easy to add new tables and features
- ✅ **Professional**: Modern UI and best practices
- ✅ **Educational**: Clear code structure for learning

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with both SQLite and MySQL
5. Submit a pull request

## 📄 License

This project is created for educational purposes in the CSE303 Database Management course.

## 📞 Support

For questions or issues related to this project, please contact your course instructor or teaching assistants.

---

**Note**: This is a template structure. You can modify the database schema, add new features, and customize the UI based on your specific project requirements.
