def TempToFahrenheit(c):
    Fahrenheit = (c * 9/5) + 32 
    print("Temperature in fahrenheit : " ,Fahrenheit,"F")

def main():
    Celsius = int(input("Enter temperature in celsius : "))

    TempToFahrenheit(Celsius)

if __name__ == "__main__":
    main()