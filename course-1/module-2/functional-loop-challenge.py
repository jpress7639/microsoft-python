# FUNCTIONAL CODE CHALLENGE

foobah = []

max_value = 50
for number in range(0, max_value + 1):
   if number % 3 == 0 and number % 4 == 0:
      print(number)
      foobah.append(number)
print(foobah)