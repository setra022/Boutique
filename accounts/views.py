from django.shortcuts import redirect, render

from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        email = request.POST.get("email")
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
        login(request, user)
        return redirect('store:index')
    return render(request, 'accounts/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('store:index')
    return render(request, 'accounts/signin.html')

def logout_user(request):
    logout(request)
    return redirect('store:index')
