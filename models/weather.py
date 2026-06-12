class Weather():
    """
    Simple weather model representing basic weather data for a city.
    """

    def __init__(self, city, temperature, condition):
        self.city = city
        self.temperature = temperature
        self.condition = condition
