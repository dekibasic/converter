print("Welcome in converter. Here you can convert kilometres in miles!")

km_to_mile = 0.62137119223733

while True:
    km = int(input("Enter number of km: "))
    print(km * km_to_mile)

    repeat = input("Do you want to convert again [y/n]?")
    if repeat == "y":
        print
    elif repeat == "n":
        print("Thank you for using my converter.")
        break
    else:
        print("Error, unknown operation")