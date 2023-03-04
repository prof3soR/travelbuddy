from django.shortcuts import render
from django.views import View
from .models import *
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
        return render(request,'login.html')
    
class registration(View):
    def get(self,request):
        return render(request,'registration.html')
    def post(self,request):
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        password=request.POST.get("password")
        user=profile(username=name,mobile=mobile,password=password)
        user.save()
        return render(request,'registration.html')
def get_todo(destination_name,duration,type):
    import os
    import openai

    openai.api_key = "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"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="List out to do things in {destination} for {duration} days with {type}".format(destination=destination_name,duration=duration,type=type),
    temperature=0,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
      
    return response.choices[0].text
          

from django.template import Template, Context
class home(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        destination_name=request.POST.get("Destination_name")
        duration=request.POST.get("time")
        type=request.POST.get("type")
        Context={"todo_list": get_todo(destination_name,duration,type)}
        return render(request,'home.html',Context)
