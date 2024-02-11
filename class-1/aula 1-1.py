'''
Enter your age and the ticket price knowing that:
people aged 10 or under and over 60 pay nothing,
over 10 or under or equal to 21 pay half and
over 21 and under 60 pay whole.
# VScode
'''
yers = int(input("enter your age;\n"))
price = float(input("enter ticket price:\n"))
result = 0,0

if yers <= 10 or yers >= 60:
   result = 0,0

elif yers > 10 and yers <= 21:
    result = price/2

elif yers > 21 and yers < 60:
    result = price

print(f"price of enter: \n{result}")