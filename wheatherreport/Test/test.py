from django.test import TestCase
from django.urls import reverse

import requests


class CityAPITestCase(TestCase):
    def test_city_list(self):
        url = reverse('city-list')  # Replace 'city-list' with your actual API endpoint URL
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"cities": ["London", "Paris", "New York"]})


def test_weather_report_exists():
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'b83b257095ff375fd543f085796ac77f'
    city = 'London'  # Replace 'London' with the city you want to check

    # Make a request to the OpenWeatherMap API
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')

    # Check the response status code
    if response.status_code == 200:
        weather_data = response.json()
        # Process and extract information from the weather_data dictionary
        # ...
        assert True
    else:
        assert False
