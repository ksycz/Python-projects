#converts Farenheits to Celsius and Celsius to Farenheit
def celsius_to_fahrenheit(c_temp):
    """Converts Celsius to Farenheits"""
    return 9.0 / 5.0 * c_temp + 32
 
def fahrenheit_to_celsius(f_temp):
    """Converts Farenheits to Celsius"""
    return (f_temp - 32.0) * 5.0 / 9.0


def temp_converter():
    """Let user choose one of the options and convert temperature"""
    user_decision = input("""Select one of the following options: 
    (f) - Farenheit to Celsius 
    (c) - Celsius to Farenheit
    (q) - Quit program
    """)
    while user_decision != "q":
        if user_decision == "f": 
            c_temp = float(input("Type Celsius temperature: "))
            print("Fahrenheit:", celsius_to_fahrenheit(c_temp))
            user_decision = input("option: ")
        elif user_decision == "c":
            f_temp = float(input("Type Fahrenheit temperature: "))
            print("Celsius:", fahrenheit_to_celsius(f_temp))
            user_decision = input("option: ")

temp_converter()
user_decision = input("option: ")