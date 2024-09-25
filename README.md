# MediaTrack-Webserver-API

MediTrack: Hospital Management System API
Table of Contents

Problem Identification
Problem Justification
Database System Choice
ORM Functionalities and Benefits
API Endpoints Documentation
Entity Relationship Diagram
Third-party Services
Models and Their Relationships
Database Relations
Task Allocation and Tracking

1. Problem Identification
The MediTrack API addresses the complex challenge of managing hospital operations in the digital age. It aims to streamline patient records, doctor schedules, appointments, and departmental management through a unified, accessible system.
2. Problem Justification
Modern healthcare facilities face increasing demands for efficiency, accuracy, and data management. Manual systems are prone to errors, time-consuming, and lack the ability to provide real-time insights. MediTrack solves these issues by:

Centralizing patient and doctor information
Automating appointment scheduling
Facilitating interdepartmental communication
Enhancing data security and accessibility
Improving overall operational efficiency

3. Database System Choice
PostgreSQL was chosen for this project due to its robust features:

ACID Compliance: Ensures data integrity in complex transactions.
Scalability: Handles large datasets efficiently, crucial for growing healthcare facilities.
Complex Queries: Supports advanced SQL features for intricate data analysis.
Extensibility: Allows custom functions and data types.
Concurrent Users: Manages multiple simultaneous connections effectively.

Drawbacks compared to other systems:

Higher resource consumption compared to lighter databases like SQLite.
Steeper learning curve than some NoSQL alternatives.

4. ORM Functionalities and Benefits
SQLAlchemy is used as the ORM (Object-Relational Mapping) tool, offering:

Database Abstraction: Allows switching between different SQL databases with minimal code changes.
Query Optimization: Generates efficient SQL queries.
Object-Oriented Paradigm: Represents database entities as Python objects.
Relationship Mapping: Simplifies complex database relationships.
Migration Support: Facilitates schema evolution over time.

Benefits include increased development speed, reduced boilerplate code, and improved code maintainability.
5. API Endpoints Documentation
Authentication

POST /auth/register: Register a new user

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
