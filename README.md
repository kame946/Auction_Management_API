# Auction Management System with JWT Authentication

This repository contains an Auction Management System implemented using Django, Django REST framework, and JWT authentication. It consists of two microservices: User Registration and Authentication, and Auction Management. This system supports two types of users: Admin users with full CRUD (Create, Read, Update, Delete) access to auctions and Normal users who can only view active auctions.

## Features

- User Registration and Authentication using JWT (JSON Web Tokens).
- Admin users can perform CRUD operations on auctions.
- Normal users can only view active auctions.
- Secure and scalable API endpoints for managing auctions.
- Built-in authentication and authorization mechanisms.
- Easy-to-use and well-documented APIs.

## Technologies Used

- Django: A high-level Python web framework.
- Django REST framework: A powerful and flexible toolkit for building Web APIs.
- JWT (JSON Web Tokens): For secure user authentication.
- Other libraries and dependencies as required.

## Installation

To set up and run this project locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/auction-management-system.git
   ```

2. Create a virtual environment and install the required dependencies:
   ```bash
   cd auction-management-system
   python -m venv venv
   source venv/bin/activate (or venv\Scripts\activate on Windows)
   pip install -r requirements.txt
   ```

3. Configure your database settings in settings.py and perform migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```


