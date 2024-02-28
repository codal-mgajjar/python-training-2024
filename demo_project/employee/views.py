from django.shortcuts import render, redirect
from .models import Employee
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from .forms import EmployeeForm

# Create your views here.


def show_employee(request):
    employees = Employee.objects.all()
    return render(request, "employee/employee_list.html", {"employees": employees})


def add_employee(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_no = request.POST.get("phone_no")
        profile_photo = request.FILES.get("profile_photo")

        e = Employee()
        e.name = name
        e.email = email
        e.phone_no = phone_no
        if profile_photo:
            file_name = default_storage.save(
                f"profile_photos/{profile_photo.name}",
                ContentFile(profile_photo.read()),
            )
            e.profile_photo = file_name

        e.save()
        return redirect("show_employee")
    return render(request, "employee/add_employee.html", {})

    # if request.method == 'POST':
    #     form = EmployeeForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('show_employee')
    # else:
    #     form = EmployeeForm()
    # return render(request, 'employee/add_employee.html', {'form': form})


def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    employee.delete_employee()

    return redirect("show_employee")
