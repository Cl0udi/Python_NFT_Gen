# from PIL import Image

# background = Image.open("test1.png")
# foreground = Image.open("test2.png")

# background.paste(foreground, (0, 0), foreground)
# background.show()

import heapq
  
# initializing list 
li1 = [6]
  
# using heapify() to convert list into heap
heapq.heapify(li1)
  
# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(10, li1))
  
# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))