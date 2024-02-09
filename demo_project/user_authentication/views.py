from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.


@login_required
def home(request):
    return render(request, "home.html",{})


def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("user_authentication:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# @login_required
# def logout(request):
#     return render(request,'registration/login',{})

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username,password= password)
    if user is not None:
        login(request,user)
        return redirect("user_authentication:home")

    else:
        error_message = "Invalid credentials"
    return render("user_authentication:login", {"error_message":error_message}) 