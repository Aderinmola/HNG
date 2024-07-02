from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class IpappViewSet(APIView):
    def get(self, request, *args, **kwargs):
        visitor_name = request.GET.get('visitor_name', 'Guest')

        req_headers = request.META
        # print("META", req_headers)
        x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
        print("F_META", x_forwarded_for_value)

        if x_forwarded_for_value:
            ip_addr = x_forwarded_for_value.split(',')[-1].strip()
        else:
            ip_addr = req_headers.get('REMOTE_ADDR', None)
        
        print("IP_ADDR", ip_addr)

        city = ""
        temp = ""

        if ip_addr == "127.0.0.1":
            city = "local"
            temp = "local"
        else:
            
            url = f"http://ip-api.com/json/{ip_addr}"
            print("URL", url)
            res = requests.get(url)
            location_data_one = res.text
            location_data = json.loads(location_data_one)
            city = location_data["city"]

            # Access environment variables
            apiKey = os.environ.get("API_KEY")
            weatherURL =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
    
            response = requests.get(weatherURL)
            data = response.json()
            temp = data["main"]["temp"]
            
        message =f"Hello, {visitor_name}!, the temperature is {temp} degrees Celcius in {city}"
        return Response(
                        {
                            "client_ip":ip_addr,
                            "location":city,
                            "greeting": message
                        }, 
                        status=status.HTTP_200_OK)
