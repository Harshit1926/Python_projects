def convert_length(value,from_unit,to_unit):
    all_units={ 'meters':1, 'kilometers':1000, 'miles':1609.34, 'feets':0.3048, 'centimeters':0.01 }
    if from_unit not in all_units or to_unit not in all_units:
        raise ValueError("Unsupported unit entered")
    elif from_unit==to_unit:
        return value
    return value*all_units[from_unit]/all_units[to_unit]

def convert_weight(value,from_weight,to_weight):
    all_units={ 'grams':1, 'kilograms':1000, 'pounds':453.592, 'ounce':28.3495, 'short ton':907185 }
    if from_weight not in all_units or to_weight not in all_units:
        raise ValueError("Unsupported unit entered")
    elif from_weight==to_weight:
        return value
    return value*all_units[from_weight]/all_units[to_weight]

def convert_temperature(value,from_unit,to_unit):
    if from_unit==to_unit:
        return value
    if from_unit=='celsius' and to_unit=='kelvin':
        return value+273.15
    elif from_unit=='celsius' and to_unit=='fahrenheit':
        return ( 9/5*value)+32
    elif from_unit=='kelvin' and  to_unit=='celsius':
        return value-273.15
    elif from_unit=='kelvin' and to_unit=='fahrenheit':
        return (value-273.15)*1.8+32
    elif from_unit=='fahrenheit' and to_unit=='celsius':
        return (value-32)*5/9
    elif  from_unit=='fahrenheit' and to_unit=='kelvin':
        return (value-32)/1.8+273.15
    else:
        raise ValueError("Unsupported units entered")
    
def main():
    title="UNIT CONVERTER"
    print(title.center(50))

    option=print("""Type 1 for Length converter
Type 2 for Weight converter
Type 3 for Temperature converter
          """)
    
    while True:
        try:
            choice=int(input("Enter Your Choice from (1/2/3):"))
            if choice in [1,2,3]:
                break
            else:
                print("Enter a Number Between 1 and 3")
        except ValueError:
            print("Enter a valid Integer")

    if choice==1:
        print("You have Chosen Length Converter")

        value=float(input("Enter your Value:"))
        from_unit=input("From Unit (meters , kilometers , miles , feets , centimeters): ").lower()
        to_unit=input("To Unit (meters , kilometers , miles , feets , centimeters): ").lower()
        result=convert_length(value,from_unit,to_unit)
        print(f"The conversion of {value} from {from_unit} to {to_unit} is {result}")

    elif choice==2:
        print("You have Chosen Weight Converter")

        value=float(input("Enter your Value:"))
        from_weight=input("From Unit (grams , kilograms , pounds , ounce ,short ton): ").lower()
        to_weight=input("To Unit (grams , kilograms , pounds , ounce ,short ton): ").lower()
        result=convert_weight(value,from_weight,to_weight)
        print(f"The conversion of {value} from {from_weight} to {to_weight} is {result}")
    
    elif choice==3:
        print("You have chosen Temperature Converter")

        value=float(input("Enter your Value:"))
        from_unit=input("From Unit (celsius , kelvin , fahrenheit): ").lower()
        to_unit=input("To Unit (celsius , kelvin , fahrenheit): ").lower()
        result=convert_temperature(value,from_unit,to_unit)
        print(f"The conversion of {value} from {from_unit} to {to_unit} is {result}")
    
   
main()

    

