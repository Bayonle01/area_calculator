import AREAS
print("="*50)
print("="*10,"WELCOME TO CALCULATOR","="*10)
print("="*50)
print("Choose from the available shapes")

ShapesArea =  """
                 1.Rectangle
                 2.Triangle
                 3.Square
                 4.Cone
                 5.Trapezium
                 6.Circle
                 7.Quit
              """
print(ShapesArea)
while True:
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("u are supposed to input integer")
        break
    if choice == 1:
        AREAS.rectangle()
    elif choice == 2:
        AREAS.Triangle()
    elif choice == 3:
        AREAS.Square()
    elif choice == 4:
        AREAS.Cone()
    elif choice == 5:
        AREAS.Trapezium()
    elif choice == 6:
        AREAS.Circle()
    elif choice == 7:
        quit()
    else:
         break
