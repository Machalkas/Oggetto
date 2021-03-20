from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Stream
from Shop.models import Shop, Goods
from Shop.forms import GoodsForm
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

def createGoods(request):
    try:
        sh=Shop.objects.get(user=request.user)
    except:
        return redirect("/shop/create")
    if request.method=="POST":
        form=GoodsForm(request.POST)
        if form.is_valid():
            stream=form.save()
            stream.shop=sh
            stream.save()
            return redirect("/streams/view/"+str(stream.id)) 
    else:
        form=GoodsForm()
    return render(request, 'Stream/create.html', {'form':form})



def view(request, st_id):
    try:
        st=Stream.objects.get(id=st_id)
    except:
        return JsonResponse({"error":"Стрим не найден"}, status=400)
    goods=[]
    stream=model_to_dict(st)
    for i in Goods.objects.filter(stream=st):
        goods.append(model_to_dict(i))
    return JsonResponse({"stream":stream,"goods":goods})

