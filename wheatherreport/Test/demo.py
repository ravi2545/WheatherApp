import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'b83b257095ff375fd543f085796ac77f'
city = 'Amalapuram'  # Replace 'London' with the city you want to check

# Make a request to the OpenWeatherMap API
response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')

# Check the response status code
if response.status_code == 200:
    weather_data = response.json()
    # Process and extract information from the weather_data dictionary
    # ...
    print(weather_data)
    # print(f"Weather report for {city} exists.")
else:
    print(f"Weather report for {city} does not exist or there was an error.")
