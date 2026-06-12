# Why Algorithms Matter 

# They are the problem-solving powerhouses behind countless tasks in the digital world

# Data structures - the ways we organize data for algorithms to process
# The right data structure can make the algorithm work faster 

# The efficiency factor: Time, space, and Big O
# this means how much time and space (or memory) an algorithm needs to solve a problem.

def simple_sort(cards):
  sorted_cards = []
  while cards:
    lowest_card = min(cards)  
    sorted_cards.append(lowest_card)
    cards.remove(lowest_card)
  return sorted_cards

# This method is simple but it would take forever if this was a massive amount of cards

# Quicksort would be much faster, example below: 

def quicksort(cards):
  if len(cards) < 2:
    return cards  # Base case: Already sorted if 0 or 1 element
  else:
    pivot = cards[0]  # Choose first card as pivot
    less = [i for i in cards[1:] if i <= pivot]
    greater = [i for i in cards[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
  
# Quicksort breaks the problem down by choosing a "pivot" element 
# and partitioning the rest of the cards into those less than or equal to the pivot 
# and those greater than the pivot.

# It then recursively sorts the "less than" and "greater than" sub-lists, 
# ultimately combining them with the pivot for a fully sorted result.

# Big O Notation
# Big O is a way to measure and express how an 
# algorithm's performance changes as the amount of data it's dealing with increases.

# IMPACT 

# Navigation apps: Ever wondered how your phone's GPS app finds the fastest route to your destination? 
# It's all thanks to graph algorithms. 
# These algorithms model your location and destination as points on a map, with roads as connections. 
# By analyzing this graph, the algorithm can quickly calculate the shortest path, saving you time and frustration in traffic.

# Streaming recommendations: When Netflix or Spotify suggests a new show or song you might enjoy, 
# it's not magic. It's machine learning algorithms at work. 
# These algorithms analyze your viewing or listening history, 
# compare it to millions of other users, and use that data to predict what you might like. 
# It's like having a personal DJ or film curator in your pocket!

# Medical imaging: Algorithms are even revolutionizing healthcare. 
# In medical imaging, image processing algorithms analyze scans (like X-rays or MRIs) 
# to detect subtle patterns that might indicate a disease. 
# This helps doctors make more accurate diagnoses and develop personalized treatment plans.


