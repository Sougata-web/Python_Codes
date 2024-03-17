fruit=input("Input the fruit(only banana):\t")
fruit=fruit.lower()
color=input("Enter the fruit color(green, yellow, brown):\t")
color=color.lower()
if fruit=="banana":
    if color == "green":
        print("Banana is unripe.")
    elif color=="yellow":
        print("Banana is ripe")
    elif color == "brown":
        print("Banana is over ripe")
    else:
        print("Rotten")