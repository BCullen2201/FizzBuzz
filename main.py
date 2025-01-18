#!/usr/bin/env python3

def createList():
    numbers = []
    for i in range(1,101):
        numbers.append(i)

    return numbers

def doFizzBuzz(list):
    for j in list:
        if j % 3 == 0:
            print("Fizz", end='')
            if j % 5 == 0:
                print("Buzz")
            else:
                print("\n", end='')
        else:
            print(j)
            

def main():
    doFizzBuzz(createList())

if __name__ == "__main__":
    main()

