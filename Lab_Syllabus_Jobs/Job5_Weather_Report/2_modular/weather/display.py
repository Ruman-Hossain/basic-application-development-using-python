def print_report(data):
    """Print the basic weather data from the API dictionary."""
    print("----- Weather Report -----")
    print("City        :", data["name"], ",", data["sys"]["country"])
    print("Temperature :", data["main"]["temp"], "°C")
    print("Feels like  :", data["main"]["feels_like"], "°C")
    print("Humidity    :", data["main"]["humidity"], "%")
    print("Condition   :", data["weather"][0]["description"])
    print("Wind speed  :", data["wind"]["speed"], "m/s")
