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

from django.http import QueryDict
import json
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

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
        print(request.query_params["token"])
        try:
            tk=request.query_params["token"]
            t=Token.objects.get(key=tk)
            u=t.user
            sh=Shop.objects.get(user=u)
        except ZeroDivisionError:
            print("нет магазина")
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        st = Stream.objects.filter(shop=sh)
        ser=StreamSerializers(st, many=True)
        s=ser.data
        x=Response(s)
        x["Access-Control-Allow-Origin"]="*"
        return x

class create(APIView):
    def post(self, request):
        try:
            n=request.data
            if type(n)==QueryDict:
                n=n.copy()
                n=json.loads(n.popitem()[0])
                print(n)
            tk=n["token"]
            # u=User.objects.get(id=t)
            t=Token.objects.get(key=tk)
            u=t.user
            sh=Shop.objects.get(user=u)
        except:
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        st=StreamSerializers(data=n["data"])
        if st.is_valid():
            x=st.save()
            x.shop=sh
            x.save()
            for i in n["goods"]:
                gd=GoodsSerializers(data=i)
                if gd.is_valid():
                    s=gd.save()
                    s.shop=sh
                    s.stream=x
                    s.save()

            x=Response({"stream_id":x.id},status=201)
            x["Access-Control-Allow-Origin"]="*"
            return x
        x=Response(status=400)
        x["Access-Control-Allow-Origin"]="*"
        return x


class get(APIView):
    def get(self, request):
        # print(request.query_params["token"])
        try:
            stream_id=request.query_params["stream"]
            # u=User.objects.get(id=request.query_params["token"])
            # sh=Shop.objects.get(user=u)
        except:
            print("нет магазина")
            x=Response({"error":""}, status=400)
            x["Access-Control-Allow-Origin"]="*"
            return x
        st = Stream.objects.get(id=stream_id)
        ser=StreamSerializers(st, many=False)
        s=ser.data
        gd=Goods.objects.filter(stream=st)
        sgd=GoodsSerializers(gd, many=True)
        g=sgd.data
        x=Response({"stream":s, "goods":g})
        x["Access-Control-Allow-Origin"]="*"
        return x

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })