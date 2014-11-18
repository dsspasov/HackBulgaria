import requests
import sqlite3
from Client import Client
import time
import smtplib
import hashlib
import uuid


conn = sqlite3.connect("bank.db")
cursor = conn.cursor()
password = 'alabala'


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                number_wrong_pass INTEGER DEFAULT 0,
                last_block REAL DEFAULT 0)'''

    cursor.execute(create_query)


def send_email(msg):
    fromaddr = 'hahahaaaa@gmail.com'
    toaddrs = 'balabala@gmail.com'

    message = 'Enter you message here\n' + msg

    username = 'dsspasov94'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def making_authentication_hash(name):
    seed = uuid.uuid4().hex
    return hashlib.sha256(seed.encode() + name.encode()).hexdigest()


def change_pass(new_pass, logged_user):
    print("eneter the code we send to your email")
    hash_code = making_authentication_hash(logged_user.get_username())
    send_email(hash_code)
    input_auth = input("hash_code> ")
    if input_auth == hash_code:
        update_sql = "UPDATE clients SET password = ? WHERE id = ?"
        cursor.execute(update_sql, (new_pass, logged_user.get_id()))
        conn.commit()
        print("You password is changed")


def register(username, password):
    insert_sql = "insert into clients (username, password) values (?, ?)"
    cursor.execute(insert_sql, (username, password))
    conn.commit()


def login(username, password):
    select_query = '''SELECT id, username, balance, message, number_wrong_pass, last_block
                        FROM clients WHERE username = ? AND password = ? LIMIT 1'''
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        update_query = '''UPDATE clients SET number_wrong_pass = ? WHERE username = ?'''
        cursor.execute(update_query, (0, username))
        conn.commit()

        return Client(user[0], user[1], user[2], user[3])
    else:
        select_query = '''SELECT username, number_wrong_pass, last_block
                            FROM clients WHERE username = ? LIMIT 1'''
        cursor.execute(select_query, (username, ))
        user = cursor.fetchone()
        if not user:
            return False
        else:
            if ((user[2] + 5 * 60) > time.time()):
                print("You can't login for 5 minutes")
            else:
                number_pass = user[1] + 1
                update_query = '''UPDATE clients SET number_wrong_pass = ? WHERE username = ?'''
                cursor.execute(update_query, (number_pass, username))
                conn.commit()
                if number_pass == 5:
                    block = time.time()
                    update_query = '''UPDATE clients SET number_wrong_pass = ?, last_block = ?
                                        WHERE username = ?'''
                    cursor.execute(update_query, (number_pass, block + 5 * 60, username))
                    conn.commit()

        return False


def deposit(money, logged_user):
    select_query = "SELECT balance FROM clients WHERE id = ?"
    cursor.execute(select_query, (logged_user.get_id(), ))
    user = cursor.fetchone()
    balance = user[0]
    balance += money
    update_query = '''UPDATE clients SET balance = ? WHERE id = ?'''
    cursor.execute(update_query, (balance, logged_user.get_id()))
    conn.commit()
    return Client(logged_user.get_id(),
                  logged_user.get_username(), balance, logged_user.get_message())


def display_balance(logged_user):
    select_query = "SELECT balance FROM clients WHERE id = ?"
    cursor.execute(select_query, (logged_user.get_id(), ))
    user = cursor.fetchone()
    return user[0]


def withdraw(money, logged_user):
    current_balance = display_balance(logged_user)
    if current_balance < money:
        print("You can't get so much money")
        return logged_user
    else:
        current_balance -= money

        update_query = '''UPDATE clients SET balance = ? WHERE id = ?'''
        cursor.execute(update_query, (current_balance, logged_user.get_id()))
        conn.commit()
        return Client(logged_user.get_id(),
                      logged_user.get_username(), current_balance, logged_user.get_message())
