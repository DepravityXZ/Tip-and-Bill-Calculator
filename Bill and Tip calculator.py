# Bill and Tip calculator
total_bill = int(input("Please enter the bill amount "))
tip = int(input("Please enter the percentage you wish to tip "))
people = int(input("How many people are paying? "))
tip_amount = tip / 100
final_amount = total_bill + (total_bill * tip_amount)
per_person = final_amount / people
final_bill = round(per_person,2)
print(f"The final bill per person is {final_bill}")
