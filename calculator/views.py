from django.shortcuts import render

# Create your views here.
def home(request):
    result=None

    if request.method=="POST":
        num1 = float(request.POST.get("num1",0))
        num2= float(request.POST.get("num2",0))
        operation = request.POST.get("operation")

        if operation == "add":
            result=num1+num2
    return render(request, "calculator/home.html",{"result":result})
