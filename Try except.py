while True:
    try:
        x = int (input("Input an integer: "))
        print(x)
    except ValueError:
        print("Something wrong ... Please try agian")