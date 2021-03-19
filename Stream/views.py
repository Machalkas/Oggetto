from django.shortcuts import render, redirect
from .models import Stream
from Shop.models import Shop

def manage(request):
    try:
        sh=Shop.objects.get(user=request.user)
    except:
        return redirect("/shop/create")
    st=Stream.objects.filter()
