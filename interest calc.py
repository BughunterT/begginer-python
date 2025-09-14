principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("please enter principle:"))
    if principle <= 0:
        print("principle cant be less than or equal zero")


while rate <= 0:
    rate = float(input("please enter rate:"))
    if rate <= 0:
        print("rate cant be less than or equal zero")


while time <= 0:
    time = float(input("please enter time:"))
    if time <= 0:
        print("time cant be less than or equal zero")

total = principle * pow((1 + rate/100), time)

print(f"balance after {time :.0f} year/s {total :.2f}")
