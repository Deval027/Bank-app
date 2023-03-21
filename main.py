import random
import pandas as pd
comeback = False
users = pd.DataFrame(columns=['user', 'password', 'account', 'balance'])

while True:
    print("---Welcome to bankingOS---\n")
    print("1.-New user(log in)\n2.-Already registered(sign in)")
    Main_menu = input("select an option: ")
    if Main_menu.isdigit():
        Main_menu = int(Main_menu)
        if Main_menu in range(1,3):
            pass
        else:
            print("Enter a valid option")
    if Main_menu == 1:
        while True:
            user = input("Enter your username(12 characters max): ")
            if len(user) > 12:
                print("username can only be less than 12 characters")
            else:
                password = input("Enter your password (8 characters minimum): ")
                if len(password) < 8 and len(password) >  20:
                    print("Password can only be between 8 and 20 characters")
                else:
                    print("Registered successfully")
                    Account_number = random.randint(100000, 999999)
                    account_number = str(Account_number)[:3] + " " + str(Account_number)[3:]
                    new_line = {'user': user,'password': password,'account':account_number,'balance': 0}
                    users = users.append(new_line, ignore_index=True)
                    users.to_csv('users.csv', index=True)
                    print("Your number account is: "+account_number)
                    comeback = True
                    break
            if comeback:
                break
    if Main_menu == 2:
        while True:
            users = pd.read_csv('users.csv')
            login = input("Enter your username: ")
            login_password = input("Enter your password: ")
            if ((users['user'] == login) & (users['password'] == login_password)).any():
                break
            else:
                print('Wrong username or password')

        break

while True:
    users = pd.read_csv('users.csv')
    print("---YOUR ACCOUNT---\n")
    acc = users.loc[users['user'] == login, 'account'].values[0]
    print(f'Welcome: {login}    Account: {acc}')
    option = input("1.-Check balance\n2.-Add founds\n3.-Withdrawal\n4.-Make a deposit\n5.-Exit\nSelect an option: ")
    if option.isdigit():
        option = int(option)
        if option in range(1,6):
            pass
        else:
            print("Enter a valid option")
    if option == 1:
        balance = users.loc[users['user'] == login , 'balance'].values[0]
        balance = str(balance)
        print("Your balance is: $"+balance)
        while True:
            back = input("Press b to go back: ")
            if back == "b":
                break
        continue
    if option == 2:
        while True:
            amount = input("How much would you like to add?(100k limit): ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 10000 and amount <= 0:
                    print("Out of limit")
                else:
                    users.loc[users['user'] == login, 'balance'] += amount
                    balance = users.loc[users['user'] == login, 'balance'].values[0]
                    balance = str(balance)
                    users.to_csv('users.csv', index=True)
                    print("Your new balance is: $"+str(balance))
                    break
            else:
                print("Can't make the deposit")
    if option == 3:
        balance = users.loc[users['user'] == login, 'balance'].values[0]
        if balance == 0:
            print("Not possible to withdrawal current balance is: $"+str(balance))
            continue
        while True:
            withdrawal = input("How much would you like to withdrawal: ")
            if withdrawal.isdigit():
                withdrawal = int(withdrawal)
                if withdrawal > balance:
                    print("Withdrawal is bigger than the current balance")
                else:
                    new_balance = balance - withdrawal
                    users.loc[users['user'] == login, 'balance'] -= withdrawal
                    users.to_csv('users.csv', index=True)
                    print("withdrawal of $" + str(withdrawal),"made with success new balance is: $"+str(new_balance))
                    break
            else:
                print("Enter a valid number")
    if option == 4:
        deposit_number = input("Enter the account number you would like to deposit: ")
        account_num = users.loc[users['user'] == login, 'account'].values[0]
        if deposit_number not in users["account"].values:
            print("account not found")
        else:
            balance = users.loc[users['user'] == login, 'balance'].values[0]
            deposit = input("How much would you like to deposit: ")
            if deposit.isdigit():
                if int(deposit) > balance:
                    print("Not enough balance")
                else:
                    account_li = users.loc[users['account'] == deposit_number]
                    actual_balance = account_li.iloc[0]['balance']
                    deposit = int(deposit)
                    new_balance = actual_balance + deposit
                    users.loc[users['user'] == login, 'balance'] -= deposit
                    less = users.loc[users['user'] == login, 'balance'].values[0]
                    users.loc[users['account'] == deposit_number, 'balance'] = new_balance
                    users.to_csv('users.csv', index=True)
                    print("deposit made with success")
            else:
                print("cant make deposit")

    if option == 5:
        exit()
