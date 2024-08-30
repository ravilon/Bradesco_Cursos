import datetime
import os

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users= None
        self.file= None
        self.load()
        
    def load(self):
        # get actaul main.py path
        
        # concats with filename before open file
        
        self.file = open(self.filename, 'r')
        
        self.users = {}
        for line in self.file:
            email, password, name, created= line.strip().split(';')
            self.users[email] = (password, name, created)
        self.file.close()
        
    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1 
        
    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1
        
    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else: 
            return False
    
    def save(self):
        with open(self.filename, 'w') as f:
            for users in self.users:
                f.write(users + ';' + self.users[users][0] + ';' + self.users[users][1] + ';' + self.users[users][2] + '\n')
                
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(' ')[0]
            