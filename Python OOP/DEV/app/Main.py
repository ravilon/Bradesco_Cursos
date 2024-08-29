from Client import Client
from Account import Account

class Main:
    pass

client = Client("Rávilon", "77981235945")

print ("Hello", client.getName(), "bellow is your account information: ")

account = Account(client.getName(), 6969, 0)

print ("Owner: ", account._owner, "\nNumber: ", account._number, "\nBalance: ", account.balance)

account.balance = 1000

print ("Owner: ", account._owner, "\nNumber: ", account._number, "\nBalance: ", account.balance)