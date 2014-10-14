#pizza.py
from time import time
from datetime import datetime

def get_from_file(file_name):
    orders = {}
    file_name = "orders/"+file_name
    file = open(file_name,"r")
    content = file.read().split('\n')
    for index in range(len(content)-1):
        line_l = content[index].split('-')
    #for line in content:
    #    line_l=line.split("-")
    #    print(line_l)
        orders[line_l[0]] = float(line_l[1])
    return orders
def take(name, price, orders):
    if name not in orders:
        orders[name] = float(price)
    else:
        orders[name] += float(price)
    print ("Taking order from %s for %s" % (name , price))
    return orders
def status(orders):
    for each in orders:
        print(each+'-'+str(orders[each]))
def save(orders):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    file_name = "orders/orders"+stamp
    file = open(file_name,"w")
    orders_for_save=''
    for each in orders:
        orders_for_save = orders_for_save + (each+'-'+str(orders[each]))+'\n'
    file.write(orders_for_save)
    file.close()
    print("Saved the current order to orders" + stamp)
def list_files(files):
    import os
    for file in os.listdir('orders'):
        files.append(file)
    for key,each in enumerate(files):
        print ('['+str(key+1)+'] - '+ str(each))
    return files
def load(orders,files,command, load_call):
    file_name = str(files[(int(command[1])-1)])
    #if not list_files_call:
    #    print("Use list command before loading")
    #if not save_call:
    #    print("You have not saved the current order.\n"+"If you wish to discard it, type "+ str((int(command[1]) )) + " load again.")
    #if load_call:    
    print('Loading '+file_name)
    orders = get_from_file(file_name)
    #if not load_call:
    #    orders.clear()
    #    orders = get_from_file(file_name)
    #    print('Loading '+file_name)
    return orders
def main():
    #------------------------
    finish_call =True
    save_call = True
    list_files_call = False
    load_call = False
    #------------------------

    #finish=False
    files = []
    orders = {}
    while(True):
        commands = input("Enter command>")
        command = commands.split(" ")
        if command[0] == 'finish':
            if  finish_call:
                print("Finishing order. Goodbye!")
                break;

            if not save_call:
                print("You have not saved your order.\nIf you wish to continue, type finish again.\nIf you want to save your order, type save")
                finish_call = True
            
            #finish = True
        elif command[0] == 'take':
            orders = take(command[1],command[2],orders)
            #take_call = True
            finish_call = False
            save_call = False
        elif command[0] == 'status':
            status(orders)
            #status_call = True
        elif command[0] == 'save':
            save(orders)
            orders.clear()
            save_call = True
            finish_call = True
            list_files_call = False
        elif command[0] == 'list':
            files.clear()
            files = list_files(files)
            list_files_call = True
        elif command[0] == 'load':
            if not list_files_call:
                print("Use list command before loading")
            elif not save_call:
                print("You have not saved the current order.\n"+"If you wish to discard it, type load "+ str((int(command[1]) )) + " again.")
                save_call = True
            else:
                orders = load(orders, files, command, load_call)
            #file_name = str(files[(int(command[1])-1)])
            #if not list_files_call:
            #    print("Use list command before loading")
            #if not save_call:
            #    print("You have not saved the current order.\n"+"If you wish to discard it, type "+ str((int(command[1]) )) + " load again.")
            #if load_call:    
            #    print('Loading '+file_name)
            #    orders = get_from_file(file_name)
            #
            #if not load_call:
            #    orders.clear()
            #    orders = get_from_file(file_name)
            #    print('Loading '+file_name)
            load_call = True
        else:
            print("Unknown command!\nTry one of the following:\ntake <name> <price>\nstatus\nsave\nlist\nload <number>\nfinish")



        #print(command)
    #print (orders)

if __name__ == '__main__':
    main()
