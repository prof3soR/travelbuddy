from django.shortcuts import render
from django.views import View
# Create your views here.
class index(View):
    def get(self,request):
        return render(request,'index.html')
class login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        user=profile(name=name,mobile=mobile)
        user.save()
        return render(request,'login.html')
class registration(View):
    def get(self,request):
        return render(request,'registration.html')