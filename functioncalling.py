import os
from typing import Dict, Literal
import google.generativeai as genai
from dotenv import load_dotenv
import json
import requests
from datetime import datetime

# Load environment variables
load_dotenv()


# Configure API keys
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

if not GOOGLE_API_KEY or not WEATHER_API_KEY:
    raise ValueError("Please set both GOOGLE_API_KEY and WEATHER_API_KEY in .env file")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

def get_weather(location: str, unit: Literal["celsius", "fahrenheit"] = "celsius") -> Dict:
    """
    Get current weather for a location using OpenWeatherMap API.
    """
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    try:
        params = {
            "q": location,
            "appid": WEATHER_API_KEY,
            "units": "metric" if unit == "celsius" else "imperial"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        if response.status_code == 200:
            return {
                "location": location,
                "temperature": data["main"]["temp"],
                "unit": unit,
                "conditions": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {"error": f"Weather API error: {data.get('message', 'Unknown error')}"}
            
    except Exception as e:
        return {"error": f"Failed to get weather: {str(e)}"}


def process_weather_query(query: str) -> str:
    """Process weather query using Gemini function calling"""
    
    # Define the weather function for Gemini
    tools = [{
        "name": "get_weather",
        "description": "Get current weather information for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City name or location"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Temperature unit",
                    "default": "celsius"
                }
            },
            "required": ["location"]
        }
    }]

    try:
        # Initialize Gemini model with the correct model name
        model = genai.GenerativeModel('gemini-2.0-flash') 
        
        # First, get the location from the query
        location_prompt = f"Extract the city or country name from this query: {query}"
        print("---------------------------")
        print("Location Prompt : ", location_prompt)
        print("---------------------------")

        location_response = model.generate_content(location_prompt)
        print("---------------------------")
        print("Location Response : ", location_response.text)
        print("---------------------------")
        location = location_response.text.strip()
        
        # Get weather data directly
        weather_data = get_weather(location=location)
        
        # Generate a natural language response
        context = f"Given the query '{query}' and weather data: {json.dumps(weather_data, indent=2)}, provide a natural language response."
        print("---------------------------")
        print("Context Prompt : ", context)
        print("---------------------------")
        final_response = model.generate_content(context)
        print("---------------------------")
        print("Context Response : ", final_response.text)
        print("---------------------------")
        return final_response.text
    
    except Exception as e:
        return f"Error: {str(e)}"
        
def main():
    print("Weather Information System (Type 'quit' to exit)")
    print("Example queries:")
    print("- What's the weather like in London?")
    print("- Tell me the temperature in New York in fahrenheit")
    print("- How's the weather in Tokyo?\n")
    
    while True:
        query = input("\nEnter your weather query: ")
        
        if query.lower() == 'quit':
            break
        
        response = process_weather_query(query)
        print("\nResponse:")
        print(response)

if __name__ == "__main__":
    main()
