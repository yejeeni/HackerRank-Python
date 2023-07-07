import math

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    max = math.pow(10, 10)
    
    if (1<=a<=max and 1<=b<=max):
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("Out of range")
