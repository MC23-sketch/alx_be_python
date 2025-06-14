import requests

# Replace this with your actual WeatherAPI key
API_KEY = "eed394ff145240ad99a92624251406"
BASE_URL = "https://api.weatherapi.com/v1/current.json"

# Ask user to input the city
city = input("Enter the city name: ")

# Create full API request URL
url = f"{BASE_URL}?key={API_KEY}&q={city}"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    location = data['location']['name']
    country = data['location']['country']
    temperature = data['current']['temp_c']
    condition = data['current']['condition']['text']

    print(f"\nWeather in {location}, {country}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")

else:
    print("Failed to retrieve data. Please check your city name or API key.")
