#We'll convert some x.yz$ value to float value and then calculate the tip.
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d=d.removeprefix("$")            
    return float(d)

def percent_to_float(p):
    
    p=p.removesuffix("%")
    return float(p)*0.01


main()
