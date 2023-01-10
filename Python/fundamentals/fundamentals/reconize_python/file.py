num1 = 42  #- variable declaration
num2 = 2.3 #- variable declaration
boolean = True #- data type - boolean
string = 'Hello World' #- data type - strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- data type - composite - list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #- composite - dictionary
fruit = ('blueberry', 'strawberry', 'banana')# - data types - tuples
print(type(fruit)) #type check
print(pizza_toppings[1]) #- data types - list - access value
pizza_toppings.append('Mushrooms') #- data types - list - add value
print(person['name'])#- data types - dictionary - access value
person['name'] = 'George' #- data type - dictionary - change value
person['eye_color'] = 'blue' #- data type - dictionary - add value
print(fruit[2]) #- data type - tuple - access value

if num1 > 45: #- conditional - if
    print("It's greater") #- log statement
else: #- conditional - else
    print("It's lower")

if len(string) < 5:#- conditional - if
    print("It's a short word!")#- log statement
elif len(string) > 15: #- conditional - else is
    print("It's a long word!")#- log statement
else:#- conditional - else
    print("Just right!")#- log statement

for x in range(5): #- for loop - sequence
    print(x)#- log statement
for x in range(2,5): #- for loop 2 start 5 stop sequence 
    print(x)#- log statement
for x in range(2,10,3): #- for loop
    print(x)
x = 0 #- variable declaration
while(x < 5): #- while loop
    print(x) #log statement
    x += 1 #log statement

pizza_toppings.pop() #- data type - list - delete value
pizza_toppings.pop(1) #- data type - list - delete value

print(person)log statement # log statement
person.pop('eye_color') #- data type - composite - dictionary - delete value
print(person) #- log statement

for topping in pizza_toppings:
    if topping == 'Pepperoni': 
        continue
    print('After 1st if statement') #- return
    if topping == 'Olives': #argument
        break

def print_hello_ten_times(): #- function 
    for num in range(10):#- parameter
        print('Hello') #- return

print_hello_ten_times() #- log statement

def print_hello_x_times(x): #- function 
    for num in range(x): #parameter
        print('Hello')#- return

print_hello_x_times(4) #- log statement

def print_hello_x_or_ten_times(x = 10): #- function
    for num in range(x): #parameter
        print('Hello') #- return

print_hello_x_or_ten_times() #- log statement
print_hello_x_or_ten_times(4)#- log statement


"""
Bonus section
"""
num3 = 72
print(num3)

fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) #- KeyError: 'favorite_team'
print(pizza_toppings[7])#- IndexError: list index out of range
print(boolean)
fruit.append('raspberry')#AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1)#- AttributeError: 'tuple' object has no attribute 'pop'