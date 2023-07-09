from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth import get_user_model, login, logout, authenticate



User = get_user_model()


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
    else:
        pass
    title = "Connexion"
    context = {
        "title": title
    }
    return render(request, "accounts/login.html", context)


def singup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('index')
    else:
        pass
    title = "S'inscrire"
    context = {
        "title": title
    }
    return render(request, "accounts/singup.html", context)


def logout_user(request):
    logout(request)
    return redirect('index')


