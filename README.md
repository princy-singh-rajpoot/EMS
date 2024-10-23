```markdown
# Employee Management System

This is a simple Employee Management System built using Django. The application allows users to view, add, filter, and remove employees. It also includes functionality to manage departments and roles within an organization.

## Features
- View all employees
- Add new employees with department and role selection
- Filter and remove employees
- Admin panel access to manage departments, roles, and employees

## Technologies Used
- Python
- Django
- SQLite (default database)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/princy-singh-rajpoot/employee-management-system.git
    ```

2. Navigate to the project directory:
    ```bash
    cd emp_project
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the application at `http://127.0.0.1:8000/`.

## Usage

1. **Home Page**: Navigate to the home page to access the application.
2. **View Employees**: Use the "View Employees" tab to see all employees.
3. **Add Employee**: Click on "Add Employee" to add a new employee by filling out the form.
4. **Filter Employees**: Use the "Filter Employee" option to filter employees based on criteria (to be implemented).
5. **Remove Employee**: Use the "Remove Employee" option to delete an employee from the list (to be implemented).

## Testing

To run the test suite, use the following command:
```bash
python manage.py test
```

The tests cover:
- Models: `Department`, `Role`, and `Employee`.
- Views: `index`, `all_emp`, `add_emp`.
- Form validation and success/error messages.

## Admin Access

You can manage departments, roles, and employees via the Django admin panel.

1. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

2. Log in to the admin panel at `http://127.0.0.1:8000/admin/`.