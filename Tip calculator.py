print("welcome to bill calculator.")
b = int(input("what was the total bill?"))
t = int(input("how much tip would you like to give? 10, 12 or 15?"))
s = int(input("how many person to split the bill?"))
bill = round(((b + (b*t/100)) / s ),2)
print("bill per person : " + str(bill))

