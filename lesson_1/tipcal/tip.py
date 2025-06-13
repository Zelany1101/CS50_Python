def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO; accept a str as input (formmated $##.##) and return the amount os a float and remove $
    # ex: $50.00 should return 50.0
    d = float(d.strip('$'))
    return d

def percent_to_float(p):
    # TODO; accept st as input (##%) and return amount of float and remove %
    # ex: 15% should return 0.15
    p = float((p.strip('%')))/100
    return p

main()
