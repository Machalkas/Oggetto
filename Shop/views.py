from django.shortcuts import render, redirect
from .forms import ShopForm
from User.models import User

def create(request):
    if not request.user.is_shop:
        return redirect("/")
    if request.method=="POST":
        form=ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop=form.save()
            shop.user=request.user
            shop.save()
            return redirect("/streams") 
    else:
        form=ShopForm()
    return render(request, 'Shop/create.html', {'form':form})
