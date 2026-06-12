# Lists from Step 1 (do not modify)
celsius_temperatures = [0, 10, 25, 32, 100]
fahrenheit_temperatures = [] 

# Convert each Celsius temperature to Fahrenheit
for celsius in celsius_temperatures:  # Start the loop (do not modify this line)
  fahrenheit = (celsius * (9/5)) + 32

  fahrenheit_temperatures.append(fahrenheit)  # Append to the list (do not modify this line)

# Print the results (including the output from Step 1 - do not modify)
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)


original_price = 100
discount_percentage = 20
sales_tax_rate = 0.08

discount_amount = original_price * (discount_percentage / 100)
print(discount_amount)
discounted_price = original_price - discount_amount
print(discounted_price)
sales_tax = discounted_price * sales_tax_rate
print(sales_tax)
final_price = discounted_price + sales_tax

print(final_price)