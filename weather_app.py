import requests

api_key = "e97a007b24a969418a8b5a2f9c778fd1"

user_input = input("Enter city: ")

weather_data = requests.get(
     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# error handling 

if weather_data.json()['cod'] == '404': # cod is the status code the API returns
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")

