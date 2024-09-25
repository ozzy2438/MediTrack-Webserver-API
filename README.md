# 🏥 MediTrack API

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## 🚀 About the Project
MediTrack API is a robust backend solution designed to manage the complex operations of modern hospitals. It unifies patient records, doctor schedules, appointments, and departmental management into a single, accessible platform.

## ✨ Features
- 👤 User Authentication and Authorization
- 🏥 Patient Management
- 👨‍⚕️ Doctor Management
- 📅 Appointment Scheduling
- 🏢 Department Management
- 📊 Detailed Reporting

## 🛠 Technologies Used
- Python 3.11
- Flask
- SQLAlchemy
- PostgreSQL
- JWT Authentication

## 💻 Getting Started
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/meditrack-api.git
   ```
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```
   flask db upgrade
   ```
4. Run the application:
   ```
   flask run
   ```

## 📚 API Documentation
For detailed API documentation, please refer to the [API.md](API.md) file.

## 🗄 Database Schema
Information about the database schema and relationships can be found in the [DATABASE.md](DATABASE.md) file.

## 🖼 Additional Resources
For a more comprehensive view of the project:

- The Entity Relationship Diagram (ERD) can be found in the `imsonia_images` directory.
- Screenshots of API testing using Insomnia are also available in the `imsonia_images` directory.

These visual resources provide a clearer understanding of the database structure and API functionality.

## 🤝 Contributing
We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Required data: {name, email, password, role}
Response: User object and JWT token


POST /auth/login: User login

Required data: {email, password}
Response: JWT token



Patients

GET /patients: List all patients
POST /patients: Add a new patient
GET /patients/<id>: View a specific patient
PUT /patients/<id>: Update patient information
DELETE /patients/<id>: Delete a patient record

[Similar documentation for Doctors, Appointments, and Departments]
6. Entity Relationship Diagram
[Insert your ERD image here]
This diagram illustrates the relationships between Patients, Doctors, Appointments, and Departments.
7. Third-party Services

Flask: Web framework for building the API
Flask-SQLAlchemy: ORM for database operations
Flask-Marshmallow: Object serialization/deserialization
Flask-JWT-Extended: JWT token handling for authentication
PostgreSQL: Database management system
Gunicorn: WSGI HTTP Server for deployment (if applicable)

8. Models and Their Relationships

Patient:

Has many Appointments
Belongs to one Department


Doctor:

Has many Appointments
Belongs to one Department


Appointment:

Belongs to one Patient
Belongs to one Doctor


Department:

Has many Patients
Has many Doctors



9. Database Relations
The database schema implements the following relations:

One-to-Many between Department and Patients/Doctors
Many-to-Many between Patients and Doctors (through Appointments)
One-to-Many between Patients/Doctors and Appointments

These relations ensure data integrity and facilitate complex queries across the system.
10. Task Allocation and Tracking
Project tasks were managed using GitHub Projects:

Planning Phase: ERD design, technology stack selection
Development Phase: Iterative implementation of models, routes, and controllers
Testing Phase: Unit testing, integration testing
Documentation Phase: API documentation, README compilation

Tasks were moved through 'To Do', 'In Progress', and 'Completed' stages, with regular commits to track progress.

## Additional Resources

For a more comprehensive view of the project:

- The Entity Relationship Diagram (ERD) can be found in the `imsonia_images` directory.
- Screenshots of API testing using Insomnia are also available in the `imsonia_images` directory.

These visual resources provide a clearer understanding of the database structure and API functionality.
