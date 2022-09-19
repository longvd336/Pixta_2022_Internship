import math

def cal_rectangle_perimeter(a, b):
    return 2*(a + b)

def cal_circle_area(r):
    return math.pi * pow(r, 2)

if __name__ == '__main__':
    f = int(input("choose function: \n\
        0. cal_rectangle_perimeter  1. cal_circle_area \nPlease enter an integer:"))

    if f == 0:
        a = int(input("Input value a: "))
        b = int(input("Input value b: "))
        result = cal_rectangle_perimeter(a, b)
    elif f == 1:
        r = int(input("Input value r: "))
        result = cal_circle_area(r)
    else:
        result = "Wrong input"
    print(f"\nResult: {result}")
