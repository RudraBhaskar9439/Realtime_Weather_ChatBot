
# Weather Information System with Gemini AI
A Python application that combines OpenWeatherMap API with Google's Gemini AI for natural language weather queries.

# 🎯 Features
🌍 Real-time weather data retrieval

🤖 Natural language processing with Gemini AI


🌡️ Support for both Celsius and Fahrenheit


🔄 Interactive query system

📊 Similarity-based content retrieval

🗺️ Global location support

# 📋 Prerequisites

Python 3.8+

Google Gemini API key

PDF documents and/or images to process

# 🛠️ Installation
## 1. Clone the repository
```python
git clone <your-repo-url>
cd <your-repo-directory>
```
## 2. Install required packages
```python
pip3 install google-generativeai python-dotenv requests
```
## 3. Create a .env file:
```python
touch .env
```

## 4. Add your API keys to .env:
```python
GOOGLE_API_KEY=your_gemini_api_key_here
WEATHER_API_KEY=your_openweathermap_api_key_here
```

# 📁 Project Structure
```python
.
├── functioncalling.py    # Main application file
├── .env                 # Environment variables (not tracked)
├── .gitignore          # Git ignore file
└── README.md           # Documentation
```

# 💻 Usage
1. Run the script:
```python
python3 functioncalling.py
```


2. Example queries:

```python
- What's the weather like in London?
- Tell me the temperature in New York in fahrenheit
- How's the weather in Tokyo?
```

⚙️ Core Components

Weather Data Retrieval

```python
get_weather(location: str, unit: Literal["celsius", "fahrenheit"])
```
Fetches real-time weather data

Supports temperature unit conversion

Returns comprehensive weather information

### Natural Language Processing
```python
process_weather_query(query: str)
```
Processes natural language queries

Extracts location information

Generates human-friendly responses


# ⚙️ Configuration

Customize these parameters in the code:
```python
chunk_size = 1000          # Size of text chunks
chunk_overlap = 200        # Overlap between chunks
max_history = 5           # Conversation memory size
top_k = 3                # Number of relevant chunks
```

# 🔒 Security
Never commit your .env file

Keep your API keys secure

Use environment variables for sensitive data

# 🤝 Contributing

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

# MIT License

Copyright (c) 2024 [Rudra Bhaskar]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Security Note
⚠️ Never commit your .env file or expose your API keys.

Author
[Rudra Bhaskar]