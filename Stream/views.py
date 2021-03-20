from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Stream
from Shop.models import Shop, Goods
from Shop.forms import GoodsForm
from .forms import StreamForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StreamSerializers


# def listSt(request):
#     try:
#         sh=Shop.objects.get(user=request.user)
#     except:
#         return redirect("/shop/create")
#     st=Stream.objects.filter(shop=sh)
#     return render(request, "Stream/list.html", {"streams":st})

# def create(request):
#     try:
#         sh=Shop.objects.get(user=request.user)
#     except:
#         return redirect("/shop/create")
#     if request.method=="POST":
#         form=StreamForm(request.POST)
#         if form.is_valid():
#             stream=form.save()
#             stream.shop=sh
#             stream.save()
#             return redirect("/streams/view/"+str(stream.id)) 
#     else:
#         form=StreamForm()
#     return render(request, 'Stream/create.html', {'form':form})

# def createGoods(request):
#     try:
#         sh=Shop.objects.get(user=request.user)
#     except:
#         return redirect("/shop/create")
#     if request.method=="POST":
#         form=GoodsForm(request.POST)
#         if form.is_valid():
#             stream=form.save()
#             stream.shop=sh
#             stream.save()
#             return redirect("/streams/view/"+str(stream.id)) 
#     else:
#         form=GoodsForm()
#     return render(request, 'Stream/create.html', {'form':form})



# def view(request, st_id):
#     try:
#         st=Stream.objects.get(id=st_id)
#     except:
#         return JsonResponse({"error":"Стрим не найден"}, status=400)
#     goods=[]
#     stream=model_to_dict(st)
#     for i in Goods.objects.filter(stream=st):
#         goods.append(model_to_dict(i))
#     return JsonResponse({"stream":stream,"goods":goods})

class list(APIView):
    def get(self, request):
        # print(request.query_params["action"])
        try:
            print(request.user)
            sh=Shop.objects.get(user=request.user)
        except:
            print("нет магазина")
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        st = Stream.objects.filter(shop=sh)
        ser=StreamSerializers(st, many=True)
        x=Response(ser.data)
        x["Access-Control-Allow-Origin"]="*"
        return x

class create(APIView):
    def post(self, request):
        try:
            sh=Shop.objects.get(user=request.user)
        except:
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        st=StreamSerializers(data=request.data)
        if st.is_valid():
            x=st.save()
            x.shop=sh
            x.save()
            x=Response(status=201)
            x["Access-Control-Allow-Origin"]="*"
            return x
        x=Response(status=400)
        x["Access-Control-Allow-Origin"]="*"
        return x