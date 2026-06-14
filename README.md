# ✈️ Airline Reservation System (Python + MySQL)

## Overview

This was my high-school project for a feature-based **Airline Reservation and Information System** built using **Python** and **MySQL**.

The application allows users to register passengers, select seat classes, calculate luggage charges, generate ticket bills, cancel reservations, and allow administrators to view passenger records.

The project follows a **modular architecture**, where each feature is separated into its own Python file for easier maintenance and scalability.

---

## Features

### Passenger Registration

* Register a new passenger
* Store travel details in MySQL
* Generate ticket records

### Seat Selection

* Choose:

  * First Class
  * Business Class
  * Economy Class
* Automatically update seat price

### Luggage Billing

* Calculate additional luggage charges
* Update passenger records

### Ticket Management

* View passenger reservation details
* Generate final bill

### Reservation Cancellation

* Delete ticket information

### Admin Panel

* View all registered passengers
* Restricted access through password authentication

---

## Technologies Used

* Python 3.x
* MySQL Server
* PyMySQL
* Command Line Interface (CLI)

---

## Project Structure

```text
airline_project/
│
├── main.py
├── database.py
│
├── features/
│   ├── register.py
│   ├── seat.py
│   ├── luggage.py
│   ├── ticket.py
│   ├── cancel.py
│   └── admin.py
│
└── README.md
```

---

## Database Tables

### Tickets

Stores passenger booking information.

Fields:

* T_no
* Name
* Journey_Date
* Source
* Destination
* Seat_class
* Seat_price
* Luggage_price
* Total_amt

---

### Seat

Stores seat categories and pricing.

Example:

| Class    | Price |
| -------- | ----- |
| First    | 6000  |
| Business | 4000  |
| Economy  | 2000  |

---

### Luggage

Stores luggage pricing.

Example:

| Weight | Price_per_kg |
| ------ | ------------ |
| <=10kg | 100          |
| <=20kg | 150          |
| >20kg  | 200          |

---

## Installation

### 1. Install Python dependencies

```bash
pip install pymysql
```

---

### 2. Configure MySQL

Create a database:

```sql
CREATE DATABASE f2;
```

Update database credentials inside:

```text
database.py
```

Example:

```python
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="f2"
)
```

---

## Running the Project

Run:

```bash
python main.py
```

---

## Program Menu

```text
1. Register passenger
2. Choose seat class
3. Add luggage
4. Generate bill
5. View ticket
6. Cancel reservation
7. View passengers (Admin)
8. Exit
```

---

## Future Improvements

* Tkinter desktop GUI
* Online payment gateway
* Ticket PDF export
* Flight scheduling
* User authentication
* Email notifications
* Web dashboard

---

## Author

Anakh Taak
