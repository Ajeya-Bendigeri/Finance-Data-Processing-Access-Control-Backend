# 💰 Finance Data Processing & Access Control Backend

A production-ready backend system for managing financial records with role-based access control, built using Flask and MongoDB.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- User Registration & Login
- JWT-based Authentication
- Role-based Access Control (RBAC)
  - Viewer → Read-only access
  - Analyst → Read + insights
  - Admin → Full access

---

### 💰 Financial Records Management
- Create financial records (income/expense)
- View records with filters
- Update records
- Soft delete records
- Pagination support

---

### 📊 Dashboard APIs
- Total Income
- Total Expense
- Net Balance
- Aggregated financial insights

---

### 🛡️ Security & Validation
- Password hashing (bcrypt)
- JWT token protection
- Role-based API restrictions
- Input validation
- Soft delete (no data loss)

---

## ⚙️ Tech Stack
* Backend
- Python (Flask)
- MongoDB (MongoEngine)
- JWT Authentication
- Bcrypt (Password hashing)
* Frontend
- HTML
- CSS
- JavaScript

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd finance_backend

python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create .env file:

DB_NAME=finance_db
DB_HOST=mongodb://localhost:27017/finance_db
JWT_SECRET_KEY=super-secret-key

5️⃣ Run the Application
python app.py

Server will start at:

http://127.0.0.1:5000

6️⃣ Output 
https://drive.google.com/file/d/1y-7Kx1m8cSy73q86qHEf6KEJtg0Oqqvq/view?usp=sharing

7️⃣ API Endpoints(POSTMAN)

https://finflow-0095.postman.co/workspace/7cb4ef92-69ee-4fde-8712-6dfd6ca44c9e/collection/39615382-f4f7bc85-c663-4672-bc10-f5bc027b5e0b?action=share&source=copy-link&creator=39615382