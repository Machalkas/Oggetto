from django.shortcuts import render, redirect
from .forms import ShopForm
from User.models import User
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Shop

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ShopSerializers, GoodsSerializers
from rest_framework.authtoken.models import Token

# def create(request):
#     if not request.user.is_shop:
#         return redirect("/")
#     if request.method=="POST":
#         form=ShopForm(request.POST, request.FILES)
#         if form.is_valid():
#             shop=form.save()
#             shop.user=request.user
#             shop.save()
#             return redirect("/streams") 
#     else:
#         form=ShopForm()
#     return render(request, 'Shop/create.html', {'form':form})

# def create(request):
#     if request.method=="POST":
#         body_unicode = request.body.decode('utf-8')
#         body = json.loads(body_unicode)
#         if request.POST.get("action")=="json":
#             data=request.POST.get("data")
#             # data={'name':'','description':'', 'url':''}
#             form=ShopForm(data)
#             if form.is_valid():
#                 shop=form.save()
#                 shop.user=request.user
#                 shop.save()
#                 return JsonResponse({"ok":""})
#             else:
#                 return JsonResponse({"error":"форма не валидна"}, status=400)
# ты пидор!    
class view(APIView):
    def get(self, request):
        # print(request.query_params["action"])
        articles = Shop.objects.get(user=request.user)
        ser=ShopSerializers(articles, many=False)
        return Response(ser.data)

class create(APIView):
    def post(self, request):
        shop=ShopSerializers(data=request.data)
        if shop.is_valid():
            shop.save()
            return Response(status=201)
        return Response(status=400)

class addGoods(APIView):
    def post(self, request):
        try:
            sh=Shop.objects.get(user=request.user)
        except:
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        goods=GoodsSerializers(data=request.data)
        if goods.is_valid():
            s=goods.save()
            s.user=request.user
            s.shop=sh
            s.save()
            x=Response(status=201)
            x["Access-Control-Allow-Origin"]="*"
            return x
        x=Response(status=400)
        x["Access-Control-Allow-Origin"]="*"
        return x