#!/usr/bin/python

from termcolor import colored
import sys
import signal
import requests
import json
from flask import jsonify

def signal_handler(sig, frame):
    print()
    print(colored('Bye Bye !','magenta',attrs = ['reverse','blink','bold']))
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


flag = 0

# user should provide rest api's ports
if(len(sys.argv)==1):
    print("Usage is python3 cli.py",colored("PORT",'magenta',attrs = ['bold']),"!")
    sys.exit(0)

port = sys.argv[1]
print(" ")
print("--------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("Hello, I am the blockchain cli.How can I help?",'\U0001f916')
base_url = "http://0.0.0.0:"+port+"/"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
last_trans = 0

while(1):

    print(" ")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print(" ")
    if(flag):
        flag = 0
        print("Invalid action! Type help for help message !")
        action = input()
    else:
        print('Please select an action..press help for available actions!')
        action = input()

    if(action=='l'):
        if(last_trans!=0):
            action = last_trans
        else:
            flag = 1
            continue

    if(len(action)==0):
        flag = 1
    elif(action == 'help'):

        print(" ")
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(" ")

        print("There are six available actions listed below")
        print("")
        # first action is t <recipient_address> <amount>
        print("1) Type",colored('t <recipient_address> <amount>','red',attrs = ['reverse','bold']),"in order to create a new transaction.")
        print("   function t takes two arguments ---->")
        print("      ",colored('first argument','cyan'),"is the recipient's address")
        print("      ",colored('second argument','cyan'),"is the amount of coins to transfer")
        print("")
        # second action is view
        print("2) Type",colored('view','red',attrs = ['reverse','bold']),"in order to view all transactions contained in the last the last validated block.")
        print("")

        # third action is show mybalance
        print("3) Type",colored('show balance','red',attrs = ['reverse','bold']),"in order to view your account balance.")
        print("")

        # fourth action is help
        print("4) Type",colored('help','red',attrs = ['reverse','bold']),"in order to view this help message.")
        print("")

        # fifth action is exit
        print("5) Type",colored('exit','red',attrs = ['reverse','bold']),"in order to exit .")
        print("")

        # sixth action is exit
        print("6) Type",colored('l','red',attrs = ['reverse','bold']),"in order to execute last executed transaction .")
        print("")

    elif(action[0]=='t'):

        print(" ")
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        last_trans = action
        url = base_url+"create_transaction"
        inputs = action.split()
        address = inputs[1]
        amount = inputs[2]
        payload = {'addr':address,'amount':amount}
        payload = json.dumps(payload)
        response = requests.post(url,data=payload,headers=headers)
        if((response.json()['message'])!='Not enough'):
            print(response.json()['message'])
        else:
            print("It seems like you are broke..You should consider clicking --> https://www.youtube.com/watch?v=TeT0vNbjs5w")

    elif(action=='show balance' or action=='s'):

        print(" ")
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        url = base_url+"show_balance"
        response = requests.get(url)
        print("Your current balance is "+str(response.json()['Balance'])+ " coins !")

    elif(action=='view' or action=='v'):

        print(" ")
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        url = base_url+"view_transactions"
        response = requests.get(url)
        #print(len(response.json()['List of transactions in the last verified block'][0]))
        j=1
        if(len(response.json()['List of transactions in the last verified block'][0])==7):
            print()
            print("Transaction",colored(j,"red"))
            print()
            print(response.json()['List of transactions in the last verified block'][0])
        else:
            for i in response.json()['List of transactions in the last verified block'][0]:
                print()
                print("Transaction",colored(j,"red"))
                print()
                print(i)
                j+=1
        #print(response.json()['List of transactions in the last verified block'][0][1])

    elif(action=='exit' or action=='Exit' or action=='exit()' or action=='EXIT()' or action=='EXIT'):
        print(" ")
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        print(colored('Bye Bye !','magenta',attrs = ['reverse','blink','bold']))
        sys.exit(0)

    else:
        flag = 1
