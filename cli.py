#!/usr/bin/env python3

import os
import math

def clear(): 
    if os.name == "posix":
        return os.system("clear")
    else:
        return os.system("cls")

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("\nDivision by zero is not allowed!\n")
    
    return a / b

def modulus(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("\nModulus by zero is not allowed!\n")
    
    return a % b

def root(a: float, b: float) -> float:
    return math.pow(a, 1/b)

def exponentiation(a: float, b: float) -> float:
    return math.pow(a, b)

def screen(result: float) -> None:
    clear()
    
    print(f"{'' * 41}\n Welcome to the Python CLI Calculator! \n{'' * 41}\n\nSupported operations: +, -, , /, %, *.\nPress \"c\" for \"clear\" or \"e\" for \"exit\".\n")
    
    if result is not None:
        print(f"{result}\n")

def main() -> None:
        
    screen(0)

    result = float(input("a = "))

    while True:
        
        screen(result)
        
        try:
            op = input("+, -, *, /, %, **: ")
            
            if op not in ["+", "-", "*", "/", "%", "**", "c", "e"]:
                print("Invalid operation! Try again ...\nPlease enter a valid operation!\n")
                continue
            
            if op == 'c':
                result = 0
                continue
            elif op == 'e':
                break
        except ValueError:
            print("Invalid operation! Try again ...\nPlease enter a valid operation!\n")
            continue
        
        try:
            b = float(input("b = "))
        except ValueError:
            print("Invalid input! Try again ...\nPlease enter a valid number!\n")
            continue
        
        if op == "+":
            result = add(result, b)
        elif op == "-":
            result = subtract(result, b)
        elif op == "*":
            result = multiply(result, b)
        elif op == "/":
            try:
                result = divide(result, b)
            except ZeroDivisionError as e:
                print(e)
                continue
        elif op == "%":
            try:
                result = modulus(result, b)
            except ZeroDivisionError as e:
                print(e)
                continue
        elif op == "**":
            result = exponentiation(result, b)
        else:
            print("Invalid operation!\nPlease enter a valid operation!")
            continue

    print("Goodbye!")

if __name__ == '__main__':
    main()