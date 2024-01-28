# Weather App


A simple and elegant weather application that fetches real-time weather information for any city using the [WeatherAPI](https://www.weatherapi.com/). Stay informed about the current temperature, cloud cover, humidity, and wind direction effortlessly.

## Features

- **Real-Time Updates:** Get the latest weather details for your chosen city.
- **Temperature in Both Units:** View temperature in both Celsius and Fahrenheit.
- **User-Friendly Interface:** Easy-to-use interface for a seamless user experience.

## How to Use

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Requests library (`pip install requests`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DarakhshanMujtaba/Weather-App.git
   cd Weather-App
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the Script:**

   ```bash
   python weatherApp.py
   ```

2. **Enter the City:**

   Enter the name of the city when prompted.

3. **Explore Weather Information:**

   View the current weather, including temperature (in Celsius and Fahrenheit), cloud cover, humidity, and wind direction.

### API Key

Make sure to replace `YOUR_API_KEY` in the API URL with your personal WeatherAPI key. You can obtain a free key by signing up on the [WeatherAPI website](https://www.weatherapi.com/).

```python
url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
```

## Contributing

If you'd like to contribute, follow these steps:

1. **Fork the Repository**
2. **Create a New Branch:**

   ```bash
   git checkout -b feature/your-feature
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -am 'Add some feature'
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/your-feature
   ```

5. **Create a Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to [WeatherAPI](https://www.weatherapi.com/) for providing reliable weather data.

