# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.forms.models import model_to_dict
from .models import Stream
from Shop.models import Shop, Goods
from Shop.forms import GoodsForm
from .forms import StreamForm
from User.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StreamSerializers
from Shop.serializers import GoodsSerializers


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
        # print(request.query_params["token"])
        try:
            u=User.objects.get(token=request.query_params["token"])
            sh=Shop.objects.get(user=u)
        except:
            print("нет магазина")
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        st = Stream.objects.filter(shop=sh)
        ser=StreamSerializers(st, many=True)
        # gd=Goods.objects.filter(stream=st)
        # sergd=GoodsSerializers(gd, many=True)
        # print(ser.data)
        s=ser.data
        # s.append(1)
        # goods=[]
        # for i in sergd:
        #     goods.append(i.data)
        # s={"stream":s,"goods":goods}
        # for i in request.data["goods"]:

        x=Response(s)
        x["Access-Control-Allow-Origin"]="*"
        return x

class create(APIView):
    def post(self, request):
        try:
            u=User.objects.get(token=request.data["token"])
            sh=Shop.objects.get(user=u)
        except:
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        st=StreamSerializers(data=request.data["data"])
        if st.is_valid():
            x=st.save()
            x.shop=sh
            x.save()
            for i in request.data["goods"]:
                gd=GoodsSerializers(data=i)
                if gd.is_valid():
                    s=gd.save()
                    s.shop=sh
                    s.stream=x
                    s.save()

            x=Response(status=201)
            x["Access-Control-Allow-Origin"]="*"
            return x
        x=Response(status=400)
        x["Access-Control-Allow-Origin"]="*"
        return x






