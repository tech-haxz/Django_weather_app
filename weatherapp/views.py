from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(req):
    # print("Request: ", req.POST)
    if 'city' in req.POST:
        city = req.POST['city']
    else:
        city = 'lucknow'

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7e82dab79885d973ca8ce48f5aeb4e9a"

    ACCESS_KEY = "rXEdLFKHTtbUTZJjunUJUsIVfRr7BVVjb8VSXnTxbH4"

    query = city
    city_url = f"https://api.unsplash.com/search/photos?client_id={ACCESS_KEY}&page=1&query={query}"

    # print(image_url)

    try:
        response = requests.get(city_url).json()
        image_url = response['results'][0]['urls'].get('full')
        PARAMS = {'units': 'metric'}
        response = requests.get(url, PARAMS).json()
        # print(response)
        desc = response.get('weather')[0]['description']
        icon = response.get('weather')[0]['icon']
        temp = response['main']['temp']

        day = datetime.date.today()
        
        return render(req, 'index.html', {'description': desc, 'icon': icon, 'temp': int(temp), 'day': day, 'city': city, 'exception': False, 'imageUrl': image_url})
    except:
        exception_occured = True
        messages.error(req, "Entered Data is not available to API")
        day = datetime.date.today()
        return render(req, 'index.html', {'description': 'NA', 'icon': 'NA', 'temp': 0, 'day': day, 'city': 'City may not appropriate!!', "exception": exception_occured, 'imageUrl': ''})



# ACCESS KEY : rXEdLFKHTtbUTZJjunUJUsIVfRr7BVVjb8VSXnTxbH4 

# Secret key:  GEdVstPJnw5gjhH_x1EedFNGbyTtv-QX3IPcI9R1O64 

# Application ID: 687132 

# Request URL = https://api.unsplash.com/search/photos?client_id={ACCESS_KEY}&page=1&query={query}

