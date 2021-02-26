"""An example library for converting temperatures."""

def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = temperature_c * 1.8 + 32
    return temperature_f

def convert_f_to_k(temperature_f):
    """Convert Fahrenheit to Kelvin."""
    temperature_k = (5/9) * (temperature_f - 32) + 273.15
    return temperature_k

def convert_c_to_k(temperature_c):
    """Convert Celsius to Kelvin."""
    return temperature_c + 273.15 

def convert_k_to_c(temperature_k):
    """Convert Kelvin to Celsius"""
    return temperature_k - 273.15

def convert_k_to_f(temperature_k):
    """Convert Kelvin to Farenheit"""
    return (9/5) * (temperature_k - 273.15) + 32

def convert_f_to_all(number):
    """Convert Farenheit to Celsius and Kevin, print a user-friendly string"""
    f_to_c = convert_f_to_c(number)
    f_to_k = convert_f_to_k(number)
    print(f'The temperature {str(number)} F is:\n- {str(f_to_c)} C\n- {str(f_to_k)} k')
