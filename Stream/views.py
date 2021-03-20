from django.shortcuts import render, redirect
from .models import Stream
from Shop.models import Shop
from .forms import StreamForm

def listSt(request):
    try:
        sh=Shop.objects.get(user=request.user)
    except:
        return redirect("/shop/create")
    st=Stream.objects.filter(shop=sh)
    return render(request, "Stream/list.html", {"streams":st})

def create(request):
    try:
        sh=Shop.objects.get(user=request.user)
    except:
        return redirect("/shop/create")
    if request.method=="POST":
        form=StreamForm(request.POST)
        if form.is_valid():
            stream=form.save()
            stream.shop=sh
            stream.save()
            return redirect("/streams/view/"+str(stream.id)) 
    else:
        form=StreamForm()
    return render(request, 'Stream/create.html', {'form':form})