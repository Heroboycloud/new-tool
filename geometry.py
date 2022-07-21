# The final program
import os, sys
import circle
import rectangle

area_circle = 1
circumference_circle = 2
area_rect = 3
peri_rect = 4
quit = 5
choice = 0
def cal():
   choice = 0

   while choice != quit:

    choice = int(input("Select your choice:  "))
    if choice == area_circle:
       radius = float(input("Enter the radius: "))
       print('Area of the circle is', circle.area(radius))
    elif choice == circumference_circle:
       radius = float(input("Enter the radius : "))
       print('The circumference is ', circle.circumference(radius))
    elif choice == area_rect:
       length = float(input(" Enter the length : "))
       breadth = float(input(" Enter the breadth : "))
       print("The Area is", rectangle.area(length,breadth))
    elif choice == peri_rect:
       length = float(input("Enter length:  "))
       breadth = float(input("Enter breadth : "))
       print("Perimeter is" , rectangle.perimeter(length,breadth))
    elif choice == quit:
         print("Exiting the program ")
         sys.exit()
    else:
        print("Error: invalid input or selection")


# Now for display menu
print("=" *10,"Menu","=" *10)
print("1. Area of circle")
print("2. Circumference of circle")
print()
print("3. Area of Rectangle ")
print(" 4. Perimeter of Rectangle ")
print("5. Quit")
cal()
