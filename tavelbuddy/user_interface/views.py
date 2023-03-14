from django.shortcuts import render,redirect
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
    

def weather(location,date):
    import requests
    api_key = 'b9acf2ae226c44742e74ce22be917766'

    # Make a request to the OpenWeatherMap API
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}'
    response = requests.get(url)

    # Parse the response to get the daily weather forecast for the given date
    if response.status_code == 200:
        weather_data = response.json()
        daily_forecast = None
        for forecast in weather_data['list']:
            if forecast['dt_txt'].startswith(date):
                daily_forecast = forecast
                break
        if daily_forecast:
            # Extract the weather data you need from the daily_forecast dictionary
            # For example, you can get the temperature, humidity, and weather description as follows:
            temperature = daily_forecast['main']['temp']
            humidity = daily_forecast['main']['humidity']
            weather_description = daily_forecast['weather'][0]['description']
            return(f'Temperature: {temperature}, Humidity: {humidity}, Weather Description: {weather_description}')
        else:
            return(f'No daily forecast found for {date}')
    else:
        return('Error: Unable to get weather forecast')



          





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
            "weather" : weather(destination_name,from_date),
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
    
