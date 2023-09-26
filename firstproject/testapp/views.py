from django.shortcuts import render

def template_view(request):
    name="mounesh"
    company="fime india pvt ltd"
    salary="1500"
    return render(request,"testapp/result.html",{"name":name,"company":company,"salary":salary})

# Create your views here.
