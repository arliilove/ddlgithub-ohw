while True:
    try:
        x = input("Enter the first number: ")
        print(type(x))
        y= input("Enter the second number: ")
        print(type(y))
        value = int(x)/int(y)
        print("x/y is ",value)
    except Exception as e:
        print("Invalid input:",e)
        print("Please try again")
    else:
        break;
    finally:      #不论try子句是否发生异常，finally子句都会执行
        print("finally")
