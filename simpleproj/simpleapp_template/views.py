from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "name":"Casey Jones",
    }
    
    return render(request, "simpleapp_template/index.html", context)
