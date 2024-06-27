from datetime import datetime

subtotal = 0
amount = float(input("what is the subtotal? "))

while amount != 0:
    subtotal += amount
    amount = float(input("what is the subtotal? "))
     

today = datetime.now()
weekday = today.weekday()
weekday = 2
discount = subtotal * (10/100)
tax = subtotal * (6/100)
discounted_price = subtotal - discount
tax2 = discounted_price * (6/100)
total_price = discounted_price + tax2
total_undiscounted_price = subtotal + tax 

if subtotal >= 50 and (weekday == 1 or weekday == 2):
    print(f"You have recieved a discount of ${discount:.2f}")
    print(f"Your sales tax is ${tax2:.2f}")
    print(f"Please pay ${total_price:.2f}")

elif subtotal >= 50:
    print(f"Your sales tax is ${tax:.2f}")
    print(f"Please pay ${total_undiscounted_price:.2f}")

elif subtotal < 50 and (weekday == 1 or weekday == 2):
    qualify = 50 - subtotal
    print(f"you have just ${qualify:.2f} left to quailfy for a discount")

elif subtotal < 50:
        print(f"Your sales tax is ${tax:.2f}")
        print(f"Please pay ${total_undiscounted_price:.2f}")
