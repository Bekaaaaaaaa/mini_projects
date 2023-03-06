"====================Функции==================="
# functions - 

'''
def name_of_function():
    some_code
    return variable

name_of functions
'''

# def function():
#     print('the function is called')
#     return'makers'
# print(function())



# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# print(substract)

# variable = substract()
# print(variable)

# list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, substract()]
# print(list_)

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# def function():
#     print("i'am calling substruct function")
#     variable = substract()
#     return variable

# print(function())


# def multiply(a, b):
#     return a * b

# num1 = 70
# num2 = 10
# num3 = 2
# print(multiply(num1, num2))


# def welcome(name, last_name):
#     return f'welcome, {name} {last_name}'

# beka = input()
# beka1 = input()
# print(welcome(beka, beka1))




# def get_word(word):
#     list_letters = list(word)
#     print(list_letters)
#     return list_letters

# def get_vowels(letters):
#     vowels = ['a', 'o', 'y', 'i', 'u', 'e']
#     list_vowels = [letter for letter in letters if letter in vowels]
#     result = ''.join(list_vowels)
#     return result
# my_world = input('enter the word')
# print(get_vowels(get_word(my_world)))



# def info(name, age):
#     return f'{name} is {age} yers old'

# print(info('beka', 18))




'-----------------------task---------------------'
'6'
# num = 6
# def check(num):
#     if num % 2 == 0:
#         return("It is even number")
#     else:
#         return("It is odd number")

# print(check(num))

'7'
# def is_palindrome(str):
#     if str.upper() == str.upper()[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome('Mom')) 

'3'
# def get_type(x, y):
#     print(f'{type(x)}\n{type(y)}') #type() выводит класс параментров или аргументов
# get_type(5,'s')

'5'
# def dictionary(a,b,c):
#     for element in a,b,c:
#         print(element)
# dictionary('first', 'second', 'third')

'8'
# def max_num(a, b):
#     return max(a, b)
# print(max_num(10, 12))

'10'
# def sum_digits(input()):
#     return sum(input())

# print(sum_digits(105))

'11'
def func11(a, b, c):
    if c == 0:
        print(a + b)
    return pow(a, b, c)

print(func11(1, 2, 0))