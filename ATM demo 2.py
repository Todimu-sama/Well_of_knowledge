from datetime import datetime
from random import randint
import sys

naira = u'\u20A6'
passCount = 0

acctNumber = [23006, 21034, 20017]
nameList = ['todi', 'lani', 'moyo']
passwordList = ['passT', 'passL', 'passM']
bankAmount = [1000000, 1000000, 1000000]

# Account number generator function
def generate_acctNum(min_, max_):
    acctNum = randint(min_, max_)
    return acctNum

# Current time and date generator function
def current_date():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print('Welcome to Coal Bank')
print('Please select your desired option')
print('1. Create new account/Register')
print('2. Login to existing account')

userInput = int(input('Please select your desired option :  '))

if userInput == 1:
    print('You have decided to create a new bank account')
    name = input('Enter your first name :  ').lower()
    while not (name.isalpha()) or len(name) == 0 :
        print('Ensure your entry contains only letters or is not empty')
        name = input('Enter your first name :  ').lower()
        
    if name in nameList:
        sys.exit('You already have an account, please select the login option')
        
    else:
        password = input('Create a password for your account :  ')
        while len(password) < 4:
            print('Passowrd must be more than 3 characters long')
            password = input('Create a password for your account :  ')
        
        password_ =  input('Please retype your password for validation :  ')
        while password != password_:
            print('Incorrect password, please retype password')
            password_ =  input('Please retype your password for validation :  ')
        
        # Generate account number
        number_ = generate_acctNum(20000, 23000)
        
        initDeposit = float(input('Deposit your cash to complete the registration :  '))
        while initDeposit < 1500:
            print('You have to open the account with at least {}1500'.format(naira))
            initDeposit = float(input('Deposit your cash to complete the registration :  '))
        
    nameList.append(name)
    passwordList.append(password_)
    bankAmount.append(initDeposit)
    acctNumber.append(number_)
    
    userID = nameList.index(name)
    
    print('You have successfully created a bank account with us')
    print('Your name is {}, your account number is {}'.format(name.capitalize(), number_))
    print('Account balance : {}{}'.format(naira, initDeposit))

elif userInput == 2:
    name = input('Please enter your username :  ').lower()
    while name not in nameList:
        print('Name not in database, please try again')
        name = input('Please enter your username :  ').lower()
    
    password = input('Please enter your password :  ')
    userID = nameList.index(name)
    while password != passwordList[userID]:
        print('Please enter a correct password')
        password = input('Please enter your password :  ')
    
    print('==================================')
    print('Welcome {}'.format(name.capitalize()))
    print('Current Date :', current_date())
    print('==================================')
    print('These are available options')
    print('1. Withdraw')
    print('2. Deposit')
    print('3. Airtime recharge')
    print('4. Complaints')
    
    userInput = int(input('Select the service you want :  '))
    if userInput == 1:
        print('You have selected the Withdraw option')
        amount = int(input('How much would you like to withdraw? :  '))
            
        while amount > bankAmount[userID]:
            print('You do not have enough funds in the account, enter a lower amount')
            amount = int(input('How much would you like to withdraw? :  '))
            
        if amount <= bankAmount[userID]:
            print('Amount Successfully withdrawn : {0}{1}'.format(naira, amount))
            print('Please take your cash')
            bankAmount[userID] -= amount
            print('Remaining balance is : {0}{1}'.format(naira, bankAmount[userID])) 
        else:
            print('Please enter a valid response, thank you')
                
    elif userInput == 2:
            print('You have selected the Deposit option')
            amount = int(input('How much would you like to deposit? :  '))
            print('You have successfully deposited : %s%d' %(naira, amount))
            bankAmount[userID] += amount
            print('Current account balance :  ', naira, bankAmount[userID])
            
    elif userInput == 3:
        print('You have selected the Airtime recharge option')
        print('Recharge options available ')
        print('1. Self recharge')
        print('2. Third party recharge')
        
        input_ = int(input('Please enter  an option :  '))
        
        if input_ == 1:
            print('Self recharge option selected')
            amount = int(input('How much would you like to recharge :'))
            
            while amount > bankAmount[userID]:
                print('You do not have sufficient funds in your account')
                amount = int(input('How much would you like to recharge :  '))
            
            print('Your have successfully recharged {0}{1} worth of airtime'.format(naira, amount))
            bankAmount[userID] -= amount
            print('Remaining balance is : {0}{1}'.format(naira, bankAmount[userID]))
            
        elif input_ == 2:
            print('Third party recharge option selected')
            amount = int(input('How much would you like to recharge :'))
            while amount > bankAmount[userID]:
                print('You do not have sufficient funds in your account')
                amount = int(input('How much would you like to recharge :  '))
            phoneNumber = input('Enter the destination phone number :  ')
            
            while phoneNumber.isalpha() or len(phoneNumber) < 11:
                print('Please enter a valid phone number')
                phoneNumber = input('Enter the destination phone number :  ')
        
            print('You have successfully sent {0}{1} to {2}'.format(naira, amount, phoneNumber))   
            bankAmount[userID] -= amount
            print('Remaining balance is : {0}{1}'.format(naira, bankAmount[userID]))
        
    elif userInput == 4:
        print('You have selected the Complaints option')
        complaint = input('Please describe the nature of your complaint :  ')
        print('Your complaint has been stored and we will get back to you')
    else:
            print('Please select a valid entry')
            
print('Thank you for banking with us !!!')
        
    
        
        
    
