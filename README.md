# ☕ Coffee Shop Challenge

Welcome to the **Coffee Shop Challenge**, a Python object-oriented programming (OOP) project designed to model a simple coffee shop system with customers, coffees, and orders.

This project emphasizes core OOP principles such as encapsulation, relationships (one-to-many, many-to-many), class vs instance methods, and data validation.

---

## 🧠 Project Overview

In this system, we model three core entities:

- **Coffee**
- **Customer**
- **Order**

### Relationships:

- A **Customer** has many **Orders**
- A **Coffee** has many **Orders**
- An **Order** belongs to both a **Customer** and a **Coffee**
- Therefore, **Customers and Coffees** have a many-to-many relationship through **Orders**

---

## 🗂️ Folder Structure

```plaintext
coffee-shop-challenge/
├── Pipfile
├── Pipfile.lock
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
    ├── customer_test.py
    ├── coffee_test.py
    └── order_test.py
```

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge
```

### 2. Initialize the Python Environment

```bash
pipenv install
pipenv shell
```

---

## 🚀 Running the App

Use `debug.py` to manually run and test your objects and relationships.

```bash
python debug.py
```

To run all unit tests:

```bash
python -m unittest discover tests
```

---

## ✅ Feature Checklist

### 🧍‍♂️ Customer

- [x] `__init__(self, name)` – must be a string between 1 and 15 characters
- [x] `.name` property with validation
- [x] `.orders()` – list of this customer's orders
- [x] `.coffees()` – unique list of coffees this customer has ordered
- [x] `.create_order(coffee, price)` – creates a new order for a coffee

---

### ☕ Coffee

- [x] `__init__(self, name)` – name must be a string with at least 3 characters
- [x] `.name` property (read-only after creation)
- [x] `.orders()` – list of orders for this coffee
- [x] `.customers()` – unique list of customers who’ve ordered this coffee
- [x] `.num_orders()` – total number of orders for this coffee
- [x] `.average_price()` – average order price for this coffee

---

### 📦 Order

- [x] `__init__(self, customer, coffee, price)` – accepts a `Customer`, `Coffee`, and `price` (float between 1.0 and 10.0)
- [x] `.customer` and `.coffee` properties (read-only)
- [x] `.price` property (read-only with validation)

---

### 🌟 Bonus

- [x] `Customer.most_aficionado(coffee)` – class method that returns the customer who spent the most on a given coffee

---

## 📌 Key Concepts Covered

- Object-Oriented Design (OOP)
- Class and instance attributes/methods
- Data validation and encapsulation
- Relationships (1-to-many, many-to-many)
- Aggregation and basic analytics

---

## Author

**Your Name**
[GitHub](https://github.com/George-Dev-Web)

---

## 📃 License

This project is for educational purposes only and is licensed under the MIT License.
