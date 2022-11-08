from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        "recommand/base.html",
        )

# def home(request):
#     return render(
#         request,
#         "recommand/home.html"
#     )
