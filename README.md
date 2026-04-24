# jlb429-upb-pantherhotel
CIST1310 Final Project Deliverable

# Panther Hotel – Web-Based Booking System

## Overview

Panther Hotel is a simple web-based hotel booking system built using **Flask (Python)**. The application allows users to browse available rooms, make reservations, and enables administrators to manage hotel operations through a lightweight interface.

This project demonstrates core concepts in **web development, backend design, and database integration**, while maintaining a clean and user-friendly interface.

---

## Objectives

* Build a functional full-stack web application using Flask
* Simulate a real-world hotel booking system
* Implement CRUD operations with a database
* Practice organizing a scalable project structure
* Demonstrate backend logic and routing

---

## Features

### User Features

* View all available rooms
* Filter rooms by type and price
* Book a room with a simple form
* Receive booking confirmation

### Admin Features

* Add new rooms
* Remove or update room availability
* View all bookings
* Basic dashboard with system overview

---

## Project Structure

```
panther_hotel/
│
├── app.py                  # Main application entry point
├── config.py               # Configuration settings
├── requirements.txt        # Dependencies
│
├── /templates              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── rooms.html
│   ├── booking.html
│   ├── admin.html
│
├── /static                 # CSS and static files
│   └── style.css
│
├── /models                 # Database models
│   ├── db.py
│   ├── room.py
│   ├── booking.py
│
├── /routes                 # Application routes
│   ├── main_routes.py
│   ├── admin_routes.py
│
└── README.md
```
---

## 🗄️ Database Design

### Room Table

* id (Primary Key)
* type (Single, Double, Suite)
* price
* availability

### Booking Table

* id (Primary Key)
* room_id (Foreign Key)
* customer_name
* booking_date

---

## Core Functionality

### Room Browsing

Users can view all available rooms dynamically retrieved from the database.

### Booking System

Users can select a room and submit a booking request, which is stored in the database.

### Admin Controls

Admins (managers) can manage room listings and monitor all bookings.

---

## 📸 Screenshots

*(Add screenshots here if available)*

---

Jordan Bennett
Dr. Ken Wang
CIST1310 | System Analysis & Design

---
