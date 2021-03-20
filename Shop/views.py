from django.shortcuts import render, redirect
from .forms import ShopForm
from User.models import User
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView

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
        
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        return Response({"articles": articles})