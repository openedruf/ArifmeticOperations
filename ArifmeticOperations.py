from math import sqrt

operation = input('Choose the operation: (+ - * / sqr sqrt)')

if (operation=='+'):
    firstnum = int(input('Enter first number: '))
    secondnum = int(input('Enter second number: '))
    print('Answer: ', firstnum + secondnum)
elif (operation=='-'):
    firstnum = int(input('Enter first number: '))
    secondnum = int(input('Enter second number: '))
    print('Answer: ', firstnum - secondnum)
elif (operation=='*'):
    firstnum = int(input('Enter first number: '))
    secondnum = int(input('Enter second number: '))
    print('Answer: ', firstnum * secondnum)
elif (operation=='/'):
    firstnum = int(input('Enter first number: '))
    secondnum = int(input('Enter second number: '))
    print('Answer: ', firstnum /secondnum)
elif (operation=='sqr'):
    firstnum = int(input('Enter the number: '))
    print('Answer: ', firstnum**2)
elif (operation=='sqrt'):
    firstnum = int(input('Enter the number: '))
    print ('Answer: ', sqrt(firstnum))
else:
    print('Error. Try again.')
