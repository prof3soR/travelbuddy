from django.shortcuts import render,redirect
from django.views import View
from .models import *
# Create your views here.
def prompt_openai(prompt):
    import openai
    openai.api_key ="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"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
      
    return response.choices[0].text

class index(View):
    def get(self,request):
        return render(request,'index.html')
class login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        mobile=request.POST.get("mobile")
        password=request.POST.get("password")
        user=profile.objects.filter(mobile=mobile).values()
        name = profile.objects.filter(mobile=mobile).values()[0]['username']
        request.session['member_id'] = mobile
        if profile.objects.filter(mobile=mobile).exists():
            if user[0]["password"]==password:
                return redirect('user_profile', name=name)
            else:
                Context={"message": "Wrong password!"}
        else:
            Context={"message": "No user found!"}
        return render(request,'login.html',Context)
    
class signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        password=request.POST.get("password")
        if profile.objects.filter(mobile=mobile).exists():
            Context={"message": "User already exists with same phone number"}
        else:
            user=profile(username=name,mobile=mobile,password=password)
            user.save()
            Context={"message": "Account Successfully created!"}
        return render(request,'signup.html',Context)
    

          





class user_profile(View):
    def get(self,request, name):
        # Get the user profile using the name
        user = profile.objects.filter(username=name).values().first()
        context = {"name": user["username"], "mobile": user["mobile"]}
        return render(request,"user_profile.html", context)
        
            

class plantrip(View):
    def get(self,request):
        return render(request,'plantrip.html')
    
    def post(self,request):
        mobile=request.session['member_id']
        name = profile.objects.get(mobile=mobile)
        trip_name=request.POST.get("trip_name")
        destination_name=request.POST.get("destination")
        from_date=request.POST.get("from_date")
        duration=request.POST.get("duration")
        trip_type=request.POST.get("trip_type")
        interest=request.POST.get("interest")
        
        # Check if trip name already exists in the database
        if tripdetails.objects.filter(name=trip_name).exists():
            context = {"message": "You have already planned a trip with this name!"}
            return render(request, 'plantrip.html', context)
        import openai
        # Generate trip itinerary using OpenAI's API
        openai.api_key = "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"
        prompt = "You're planning a trip to {destination} for {duration}. Create an itinerary that includes must-do activities and places to visit each day".format(destination=destination_name,duration=duration)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        itinerary = response.choices[0].text
        
        # Send the itinerary back to the template for display
        context = {
            "trip_name": trip_name,
            "destination_name": destination_name,
            "from_date": from_date,
            "duration": duration,
            "trip_type": trip_type,
            "interest": interest,
            "itinerary": itinerary,
        }
        return render(request, 'tripsuggesions.html', context)



def mytrips(request):
    mobile=request.session['member_id']
    name = profile.objects.get(mobile=mobile)
    user_trips = tripdetails.objects.filter(username=name)
    return render(request, 'mytrips.html', {'trips': user_trips})

class tripsuggestions(View):
    def get(self,request):
        return render(request,'tripsuggesions.html')
    