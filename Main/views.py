from django.shortcuts import render

def main(request):
    return render(request, "Main/index.html")