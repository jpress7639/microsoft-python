order_total = 51

if order_total >= 50:
  print("Congratulations! You qualify for free shipping.")
else:
  print("Add more items to your cart to reach the free shipping threshold!")


# if - elif - else

points = 800

if points >= 1000:
  print("You've achieved Platinum status! Enjoy exclusive benefits.")
elif points >= 500:
  print("You're a Gold member! Thank you for your loyalty.")
elif points >= 100:
  print("Welcome to the Silver tier! Start earning rewards.")
else:
  print("You're a Bronze member. Keep shopping to earn more points!")


# decision and selection statements can nest conditions or boolean logic
# uses operators like (AND OR NOT)
# overuse or incorrect implementation can lead to code that is difficult to read

# Dictionary Mapping: When dealing with multiple choices based on a single key value, dictionaries can offer a cleaner solution. For example, instead of a long chain of elif clauses to determine shipping costs based on country codes, a dictionary can map country codes to shipping rates, making the code more concise, readable, and easier to update.

# Utilizing Python Libraries: Python offers powerful libraries like NumPy and pandas that provide optimized functions for performing conditional operations on arrays and dataframes, often significantly faster than manual implementations. Leveraging these libraries can not only improve code efficiency but also reduce development time and effort.
