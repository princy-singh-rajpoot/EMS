from django.shortcuts import render,redirect
from .models import Employee,Department,Role
from django.contrib import messages
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render (request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    # success_message = request.GET.get('success_message')
    return render(request,'view_emp.html',context,)

def add_emp(request):
    departments = Department.objects.all()
    roles = Role.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully!')
            return redirect('all_emp')  # Redirect to a view that will display after successfully adding employees
        else:
            messages.error(request, 'Failed to add employee. Please check the form for errors.')
    else:
        form = EmployeeForm()
    return render(request, 'add_emp.html', {'form': form,'departments': departments, 'roles': roles})

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')