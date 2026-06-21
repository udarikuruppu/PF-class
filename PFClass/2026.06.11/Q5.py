weight = int(input("Enter baggage weight"))
if weight <= 20:
    print("no charge")
else:
    if weight <= 30:
        charge = (weight - 20)*200
        print("extra charge is",charge)
    else:
        print("Baggage not allowed")
