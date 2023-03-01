# -*- coding: utf-8 -*-
import random
import sqlite3
comeback = False
conn = sqlite3.connect('userdata.db')
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
                    c = conn.cursor()
                    c.execute('INSERT INTO users (user, password, account_number) '
                              'VALUES (?, ?, ?)', (user, password, account_number))
                    conn.commit()
                    print("Your number account is: "+account_number)
                    comeback = True
                    break
            if comeback:
                break
    if Main_menu == 2:
        while True:
            login = input("Enter your username: ")
            login_password = input("Enter your password: ")
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE user = ? AND password = ?', (login, login_password))
            user_found = c.fetchone()
            if user_found is None:
                print('Wrong username or password')
            else:
                break
        break

while True:
    print("---YOUR ACCOUNT---\n")
    print(f'Welcome: {login}    Account: {user_found[3]}')
    option = input("1.-Check balance\n2.-Add founds\n3.-Withdrawal\n4.-Make a deposit\n5.-Exit\nSelect an option: ")
    if option.isdigit():
        option = int(option)
        if option in range(1,6):
            pass
        else:
            print("Enter a valid option")
    if option == 1:
        print("Your balance is: $"+str(user_found[4]))
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
                    new_balance = user_found[4]+int(amount)
                    c = conn.cursor()
                    c.execute('UPDATE users SET balance = ? WHERE user = ? ', (new_balance,login))
                    conn.commit()
                    print("Your new balance is: $"+str(new_balance))
                    break
            else:
                print("Can't make the deposit")
    if option == 3:
        if user_found[4] == 0:
            print("Not possible to withdrawal current balance is: $"+str(user_found[4]))
            continue
        while True:
            withdrawal = input("How much would you like to withdrawal: ")
            if withdrawal.isdigit():
                withdrawal = int(withdrawal)
                if withdrawal > user_found[4]:
                    print("Withdrawal is bigger than the current balance")
                else:
                    new_balance = user_found[4] - withdrawal
                    c = conn.cursor()
                    c.execute('UPDATE users SET balance = ? WHERE user = ? ', (new_balance, login))
                    conn.commit()
                    print("withdrawal of $" + str(withdrawal),"made with success new balance is: $"+str(new_balance))
                    break
            else:
                print("Enter a valid number")
    if option == 4:
        deposit_number = input("Enter the account number you would like to deposit: ")
        c.execute('SELECT * FROM users WHERE account_number = ?', (deposit_number,))
        account_found = c.fetchone()
        if account_found is None:
            print("account not found")
        else:
            deposit = input("How much would you like to deposit: ")
            if deposit.isdigit():
                if int(deposit) > user_found[4]:
                    print("Not enough balance")
                else:
                    new_balance = user_found[4] - int(deposit)
                    deposit_made = account_found[4] + int(deposit)
                    c = conn.cursor()
                    c.execute('UPDATE users SET balance = ? WHERE account_number = ?', (new_balance, account_found[3]))
                    c.execute('UPDATE users SET balance = ? WHERE account_number = ?', (deposit_made, deposit_number))
                    conn.commit()
                    print("deposit made with success")
            else:
                print("cant make deposit")

    if option == 5:
        conn.close()
        exit()