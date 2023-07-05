# CompanyManagement-Django

CompanyManagement-Django is a Django-based web application that serves as a management system for a company. It utilizes Django as the backend framework and incorporates HTML, CSS, Bootstrap, and JavaScript for the frontend. The default database used is SQLite3, which comes bundled with Django.

The application includes the following key features and pages:

## Pages

### Homepage
- The landing page of the application, providing an overview of the system's functionalities and navigation options.

### Admin Page
- A secure section accessible only to administrators.
- Features a dashboard providing a summary of key metrics and data related to the company.
- Allows administrators to manage employee details, such as creating, deleting, updating, and reading employee information.
- Provides the ability to generate admission cards for employees.

### Employee Page
- A section dedicated to employees of the company.
- Contains a personalized dashboard displaying relevant information, such as upcoming events, announcements, and tasks.
- Employees can view and update their personal details, such as contact information and preferences.
- Allows employees to view their fee information, including payment history and outstanding dues.
- Provides access to course details, including enrollment, progress tracking, and completion certificates.

## Authentication and User Management

The application incorporates robust authentication and user management functionalities, including:

- User registration and login mechanisms.
- Secure password storage using industry-standard hashing algorithms.
- Forgotten password recovery through a password reset feature.
- Authorization and access control, ensuring that only authenticated users can access specific pages or perform certain actions.

## Technologies Used

The following technologies have been used in the development of CompanyManagement-Django:

- Django: A powerful Python web framework for building robust and scalable applications.
- HTML: The standard markup language for creating web pages.
- CSS: The stylesheet language used for describing the presentation of a document written in HTML.
- Bootstrap: A popular CSS framework that provides pre-built components and responsive design features.
- JavaScript: A high-level programming language used for enhancing interactivity and functionality on web pages.
- SQLite3: The default database used in Django, providing a lightweight and self-contained solution.

## Installation and Setup

To set up and run the CompanyManagement-Django application, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Navigate to the project directory: `cd CompanyManagement-Django`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate the virtual environment:
   - For Windows: `venv\Scripts\activate`
   - For Unix/Linux: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Apply database migrations: `python manage.py migrate`
7. Run the development server: `python manage.py runserver`
8. Access the application by visiting `http://localhost:8000` in your web browser.

Please note that these instructions assume you have Python and Django installed on your machine.

## Contributions

Contributions to CompanyManagement-Django are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request on the repository.

## Project vedio-
youtube project video link - https://www.youtube.com/watch?v=HSAJv4b_acY&t=634s
## Image
![image](https://github.com/developerMaurya/companyManagement-Django/assets/137375643/3ea6a009-bb76-4dc0-954b-326b75f375c9)
