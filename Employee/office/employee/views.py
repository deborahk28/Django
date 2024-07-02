from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')  # Updated to match form field name
        last_name = request.POST.get('lastname')  # Updated to match form field name
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        department_id = request.POST.get('department')
        role_id = request.POST.get('role')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        # Create Employee instance and save to database
        employee = Employee(
            firstname=first_name,
            lastname=last_name,
            salary=int(salary) if salary else 0,
            bonus=int(bonus) if bonus else 0,
            department_id=int(department_id) if department_id else None,
            role_id=int(role_id) if role_id else None,
            phone=int(phone) if phone else None,
            hire_Date=datetime.now()  # Assuming hire_date is today
        )
        employee.save()
        return render(request, 'add_emp.html', {'message': 'Employee added successfully!'})

    return render(request, 'add_emp.html')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except Employee.DoesNotExist:
            return HttpResponse("Enter a valid employee ID")
    else:
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Updated to match form field name
        department = request.POST.get('department')
        role = request.POST.get('role')
        
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(firstname__icontains=name) | Q(lastname__icontains=name))
        if department:
            emps = emps.filter(department__name__icontains=department)
        if role:
            emps = emps.filter(role__name__icontains=role)
            
        context = {
            'emps': emps
        }
        
        return render(request, 'all_emp.html', context)
    
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    
    else:
        return HttpResponse("An exception occured")
