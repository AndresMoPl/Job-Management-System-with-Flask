"# Job-Management-System-with-Flask" 


A web-based Job Management System built using Flask that allows users to manage job postings, applications, and related workflows efficiently.

 Description

This project is a full-stack web application designed to handle job-related processes such as:

Creating and managing job offers
Tracking applications
Managing users (admin/candidates)
Organizing job-related data in a structured way

It is built as a learning project to practice backend development with Flask and database integration.

 * Features
 * User authentication (login/register)
 * Job posting management (CRUD operations)
 * Application tracking
 * User roles (admin / user) (if implemented)
 * Modular Flask structure
 * Tech Stack
Backend: Python + Flask
Database: MySQL (
ORM: SQLAlchemy 

* Project Structure
  
Job-Management-System-with-Flask/
│
├── app/
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   └── static/
│
├── requirements.txt
├── run.py / app.py
└── config.py



Installation

Clone the repository:

git clone https://github.com/AndresMoPl/Job-Management-System-with-Flask.git

Navigate into the project:

cd Job-Management-System-with-Flask

Create a virtual environment:

python -m venv venv
Activate the environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt



Purpose

* Practice Flask development
* Understand CRUD operations and MVC structure
* Learn how to connect backend with frontend
* Build a portfolio-ready project
