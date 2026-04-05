# Finance Tracker  
### Role-Based Personal Finance Management System  

Built with **Python · Flask · JSON**

---

## Project Overview  

Finance Tracker is a full-stack web application designed for managing personal finances with role-based access control.  

The system supports three distinct user roles — Admin, Analyst, and User — each with dedicated dashboards and permissions. All financial data is stored in a structured JSON file, and every action is logged through a per-user passbook system for transparency and auditability.

---

## Key Features  

- Role-Based Authentication (Admin / Analyst / User)  
- Income & Expense Tracking  
- Automatic Passbook (Audit Log)  
- Monthly Financial Insights (Chart.js)  
- Admin Panel for User Management  
- Analyst Dashboard for Filtering & Reports  
- Responsive Dark-Themed UI  

---

## User Roles & Permissions  

| Role     | Route       | Capabilities |
|----------|------------|-------------|
| Admin   | `/admin`   | Create, update, delete users |
| Analyst | `/analyst` | Filter and analyze transactions |
| User    | `/user`    | Manage personal transactions and view summary |

---

## Project Structure  
finance_tracker/
│
├── app.py
<br>
├── data.json
│
├── templates/
<br>
│ ├── login.html
<br>
│ ├── user.html
│ ├── admin.html
<br>
│ └── analyst.html
<br>
│
└── utils/
<br>
│ ├── core.py
<br>
│ ├── viewers.py
<br>
│ ├── transactions.py
<br>
│ ├── records_update.py
<br>
│ └── filters.py
<br>
└──

---

## Data Model  

Each user is stored as an object in `data.json`:

{
  "Name": "John Doe",
  <br>
  "DOB": "2000-01-01",
  <br>
  "Phone": "9999999999",
  <br>
  "Password": "password",
  <br>
  "Role": "user",
  <br>
  "Transactions": [],
  <br>
  "Summary": {},
  <br>
  "Passbook": []
}

## Key Components
Transactions → Income/Expense records
Summary → Auto-calculated totals
Passbook → Complete action history

## Core Modules  

### core.py  
- Data loading and saving  
- Passbook logging  
- Summary calculations  

### transactions.py  
- Add/Delete transactions  
- Automatic summary updates  

### records_update.py  
- Create, update, and delete users  

### viewers.py  
- Fetch transactions, summaries, and passbook  

### filters.py  
- Analyst-level filtering and reporting  

## API Routes

| Method   | Route                      | Role    | Description         |
| -------- | -------------------------- | ------- | ------------------- |
| GET/POST | `/`                        | All     | Login               |
| GET      | `/user`                    | User    | User dashboard      |
| POST     | `/add_transaction`         | User    | Add transaction     |
| GET      | `/delete_transaction/<id>` | User    | Delete transaction  |
| GET      | `/admin`                   | Admin   | Admin dashboard     |
| POST     | `/admin/create`            | Admin   | Create user         |
| POST     | `/admin/update`            | Admin   | Update user         |
| POST     | `/admin/delete`            | Admin   | Delete user         |
| GET      | `/analyst`                 | Analyst | Analyst dashboard   |
| POST     | `/filter`                  | Analyst | Filter transactions |
| GET      | `/logout`                  | All     | Logout              |


## Setup & Installation

    Prerequisites
    Python 3.8+
    Flask

## Run the Project

git clone <your-repo-url>
cd finance_tracker

pip install flask
python app.py

Application runs at:
http://127.0.0.1:5000

## Default Admin Setup

Add this manually to data.json before first run:
{
  "Name": "Admin User",
  "DOB": "2000-01-01",
  "Phone": "9999999999",
  "Password": "admin123",
  "Role": "admin",
  "Transactions": [],
  "Summary": {},
  "Passbook": []
}

## Default Analyst Setup

Add this manually to data.json before first run:
{
  "Name": "Analyst User",
  "DOB": "2000-01-01",
  "Phone": "9999999999",
  "Password": "analyst123",
  "Role": "analyst",
  "Transactions": [],
  "Summary": {},
  "Passbook": []
}
## UI & Design

Dark theme with consistent styling
Clean typography using Google Fonts
Smooth animations and transitions
Chart.js integration for analytics
Responsive layout for different screen sizes

## Design Decisions

### Passbook Logging

All actions are recorded to maintain a complete audit trail.

### Real-Time Summary

Summaries are recalculated after every transaction to ensure accuracy.

### Safe Deletion

User deletion requires matching Name, DOB, and Phone.

### Efficient Data Handling

Single save operation prevents duplicate writes and inconsistencies.

## Tech Stack

| Layer    | Technology        |
| -------- | ----------------- |
| Backend  | Python, Flask     |
| Frontend | HTML, CSS, Jinja2 |
| Database | JSON              |
| Charts   | Chart.js          |
| Fonts    | Google Fonts      |

## Future Improvements

Database integration (SQLite / PostgreSQL)
Token-based authentication
Export reports (PDF/Excel)
Mobile application support

## License

This project is developed for academic and internship submission purposes.

## Acknowledgment

Developed as part of a practical implementation of full-stack web development with Flask, focusing on financial tracking and role-based systems.
