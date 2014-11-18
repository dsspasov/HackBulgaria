import sql_manager
import hashlib


def hashing_pass(password):
    return hashlib.sha1(password.encode()).hexdigest()


def is_correct_pass(password):
    if len(password) < 8:
        print("password is too short")
        return False
    else:
        for symbol in password:
            if not symbol.isupper() and not symbol.isdigit():
                print("Your password must have capital letters and numbers")
                return False
    return True


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if is_correct_pass(password):
                hash_password = hashing_pass(password)
                sql_manager.register(username, hash_password)
                print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            hash_password = hashing_pass(password)
            logged_user = sql_manager.login(username, hash_password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            hash_new_password = hashlib.sha1(new_pass.encode()).hexdigest()
            sql_manager.change_pass(hash_new_password, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'deposit':
            amount_money = float(input("Enter amount: "))
            logged_user = sql_manager.deposit(amount_money, logged_user)

        elif command == 'display-balance':
            balance = sql_manager.display_balance(logged_user)
            print("Your current balance is {}".format(balance))

        elif command == 'withdraw':
            amount_money = float(input("Enter amount: "))
            logged_user = sql_manager.withdraw(amount_money, logged_user)

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("deposit - for depositing money")
            print("display-balance - for displaying balance")
            print("withdraw - for withdrawing money from the bank account")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
