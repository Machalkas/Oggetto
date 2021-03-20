from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.http import JsonResponse

def join(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            email=form.cleaned_data.get("email")
            user_pass = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=user_pass)
            logout(request)
            login(request, user)
            if user.is_shop:
                return redirect("/streams")
            else:
                return redirect("/")    
    else:
        form=SignUpForm()
    return render(request, 'User/join.html', {'form':form})

def logIn(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            user_pass=form.cleaned_data.get('password')
            user = authenticate(email=email, password=user_pass)
            if user!=None and user.is_active:
                    login(request, user)
                    # url=request.GET.get('next','/')
                    if user.is_shop:
                        return redirect("/streams")
                    else:
                        return redirect("/")   
            else:
                pass        
    else:
        return render(request, "User/index.html")
        # form = LoginForm()
    x=JsonResponse({"mes":"hui"})
    x["Access-Control-Allow-Origin"]="*"
    return x
    # return render(request, 'User/login.html', {'form':form})

def logOut(request):
    logout(request)
    return redirect("/user/login")