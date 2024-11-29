# Input: Total bill, tip percentage, and number of people
bill_amount = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Calculate the tip and total amount
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount

# Calculate each person's share
amount_per_person = total_amount / num_people

# Display the results
print("\n--- Bill Splitting Calculator ---")
print(f"Total Bill: ${bill_amount:.2f}")
print(f"Tip Percentage: {tip_percentage}%")
print(f"Total Amount (with Tip): ${total_amount:.2f}")
print(f"Each Person Pays: ${amount_per_person:.2f}")
