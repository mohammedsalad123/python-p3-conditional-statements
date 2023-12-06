#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin" and password == 1234 :
        return "Access granted"
    else:
        return"Access denied"
admin_login("sudo",223)
def hows_the_weather(temperature):
    if temperature<40 :
        return "It's brisk out there!"
    elif temperature >40 and temperature <65 :
        return "It's a little chilly out there!"
    elif temperature > 85 : 
        return"It's too dang hot out there!"


def fizzbuzz(num):
    
    if num % 3 == 0 and num % 5 == 0:
        return f"FizzBuzz"
    if num % 3 == 0 :
         return f"Fizz"
    if num % 5 == 0 :
        return f"Buzz" 


def calculator(operation, num1, num2):
    if operation == "+":
      return num1 + num2
    if operation == "-":
       return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    
