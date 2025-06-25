
# 🏠 Rent Management System

A desktop-based Rent Management System built using **Python**, **Tkinter**, and **PostgreSQL**. It allows an admin to manage tenant records including rent details, and lets tenants log in to view their own rent information.

---

## 🚀 Features

### 🔐 User Roles
- **Admin**
  - Login with hardcoded credentials
  - Add, update, and delete tenant rent records
  - View all records in a table
- **Tenant**
  - Login using username and password
  - View their own rent details
  - Export rent summary to a `.txt` file

### 📦 Core Functionalities
- CRUD operations for rent records
- Password masking
- Data validation for dates and amounts
- Export functionality for tenant data
- PostgreSQL database integration
- GUI built with Tkinter

---

## 🗂️ Project Structure

```
rent-management/
│
├── Display.py           # Main GUI logic and CRUD interface
├── User Management.py   # Login system for admin and tenant
├── CRUD_OPS.py          # Database operations using psycopg2
└── README.md            # Project documentation
```

---

## 🛠️ Tech Stack

| Layer        | Tech Used       |
|-------------|-----------------|
| Language     | Python 3.x      |
| GUI Library  | Tkinter         |
| Database     | PostgreSQL      |
| DB Library   | psycopg2        |

---

## 🧰 How to Run

### 📝 Prerequisites
- Python 3 installed
- PostgreSQL installed and running
- Required Python packages installed:
  ```bash
  pip install psycopg2
  ```

### 📦 Setup
1. Create a PostgreSQL database named `rent`
2. Update your database credentials in `CRUD_OPS.py` if needed:
   ```python
   psycopg2.connect(
       host="localhost",
       user="postgres",
       password="YOUR_PASSWORD",
       database="rent"
   )
   ```
3. Run the program:
   ```bash
   python "User Management.py"
   ```

---

## 👥 Default Credentials

| Role   | Username | Password       |
|--------|----------|----------------|
| Admin  | root     | root@postgres     |
| Tenant | Use valid USERNAME and PASSWORD from DB |

---

## 📁 Future Improvements
- Migrate to web-based version
- Add role-based dashboards
- Add rent due reminders via email
- Encrypt stored passwords
- Add cloud hosting support

---

## 💬 Author

**Knl (Krunal Asari)**  
Backend & Web Development Enthusiast
