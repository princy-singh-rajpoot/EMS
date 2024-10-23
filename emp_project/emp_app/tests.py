# test.py
from django.test import TestCase
from .models import Employee, Department, Role
from django.urls import reverse

class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="IT", location="Mumbai")

    def test_department_str(self):
        self.assertEqual(str(self.department), "IT")

class RoleModelTest(TestCase):
    def setUp(self):
        self.role = Role.objects.create(name="Developer")

    def test_role_str(self):
        self.assertEqual(str(self.role), "Developer")

class EmployeeModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="IT", location="Mumbai")
        self.role = Role.objects.create(name="Developer")
        self.employee = Employee.objects.create(
            first_name="John",
            last_name="Doe",
            dept=self.department,
            salary=50000,
            bonus=5000,
            role=self.role,
            phone=1234567890,
            hire_date="2023-01-01"
        )

    def test_employee_str(self):
        self.assertEqual(str(self.employee), "John Doe IT")

class ViewsTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_all_emp_view(self):
        response = self.client.get(reverse('all_emp'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_emp.html')

    def test_add_emp_view(self):
        response = self.client.get(reverse('add_emp'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_emp.html')
    
    def test_add_employee_post(self):
        department = Department.objects.create(name="HR", location="Pune")
        role = Role.objects.create(name="Manager")
        response = self.client.post(reverse('add_emp'), {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'dept': department.id,
            'salary': 60000,
            'bonus': 3000,
            'role': role.id,
            'phone': 9876543210,
            'hire_date': '2023-06-15'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after success
        self.assertEqual(Employee.objects.count(), 1)  # New employee added
