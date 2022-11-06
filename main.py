import sys
import random

class Iphone_Reinforcement(object):
    def __init__(self):
        self.iPhones = [
            ["iPhone", "June 29, 2007", 1, 3],
            ["iPhone 3G", "July 11, 2008", 0.95, 10],
            ["iPhone 3GS", "June 19, 2009", 0.93, 20],
            ["iPhone 4", "June 24, 2010", 0.90, 25],
            ["iPhone 4S", "October 14, 2011", 0.87, 30],
            ["iPhone 5", "September 21, 2012", 0.85, 40],
            ["iPhone 5S", "September 20, 2013",0.83, 50],
            ["iPhone 5C",  "September 20, 2013", 0.80, 60],
            ["iPhone 6 ", "September 19, 2014", 0.77, 70],
            ["iPhone 6 Plus", "September 19, 2014", 0.75, 80],
            ["iPhone 6S", "September 19, 2015", 0.72, 90],
            ["iPhone 6s Plus", "September 19, 2015", 0.7, 100],
            ["iPhone SE", "March 31, 2016", 0.66, 110],
            ["iPhone 7 ", "September 16, 2016", 0.65, 120],
            ["iPhone 7 Plus", "September 16, 2016", 0.63, 130],
            ["iPhone 8 ", "September 22, 2017", 0.6, 140],
            ["iPhone 8 Plus", "September 22, 2017", 0.55, 150],
            ["iPhone X:", "November 3, 2017", 0.5, 160],
            ["iPhone XS","September 21, 2018", 0.47, 170],
            ["iPhone XS Max", "September 21, 2018", 0.44, 180],
            ["iPhone XR", "October 26, 2018", 0.41, 190],
            ["iPhone 11", "September 20, 2019", 0.38, 200],
            ["iPhone 11 Pro", "September 20, 2019", 0.35, 230],
            ["iPhone 11 Pro Max", "September 20, 2019", 0.32, 300],
            ["iPhone 12", "October 23, 2020", 0.3, 400],
            ["iPhone 12 Mini", "October 23, 2020", 0.27, 500],
            ["iPhone 12 Pro", "October 23, 2020", 0.25, 1000],
            ["iPhone 12 Pro Max", "October 23, 2020", 0.22, 2000],
            ["iPhone 13", "September 14, 2021", 0.2, 5000],
            ["iPhone 13 Mini", "September 14, 2021", 0.17, 10000],
            ["iPhone 13 Pro", "September 14, 2021", 0.15, 20000],
            ["iPhone 13 Pro Max", "September 14, 2021", 0.05, 30000],
            ["iPhone 14", "September 16, 2022", 0.4, 50000],
            ["iPhone 14 Plus", "September 16, 2022", 0.03, 60000],
            ["iPhone 14 Pro", "September 16, 2022", 0.02, 90000],
            ["iPhone 14 Pro Max", "September 16, 2022", 0.01, 100000]
        ]
        self.current = 0  #self.iPhones[0]
        self.money = 0
        self.protection = 0
        self.protection_flag = False

    def Commanding(self, comm):
        command = comm

        var = command
        if var == "go":
            self.random_go(self.iPhones[self.current][2])
            print(f"chance: {self.iPhones[self.current][2] * 100}%")
        if var == "sell":
            self.money += self.iPhones[self.current][3]
            self.initialize()
        if var == "protection":
            self.protection_flag = True
        if var == "store":
            print("Welcome to the store, but anything you want")
            print("|protection|: you can use this before you reinforce the iPhone and can protect you from Fails")
            store_command = input()
            if store_command == "exit":
                return
            if store_command == "protection":
                self.protection += 1
                print("purchased |protection|!")
            

    def error(self, msg: str):
        print(msg)
        
    def random_go(self, percentage: int):
        if random.random() <= percentage:
            self.advance()
            print("Succed")
            print(f"current balance: {self.money}")
            print(f"current: {self.iPhones[self.current][0]}")

        else:
            if self.protection_flag:
                self.protection -= 1
                self.protection_flag = False
                print("|protectoin| protected you from Fail, you can continue reinforceing!")
                print(f"current balance: {self.money}")
                print(f"current: {self.iPhones[self.current][0]}")
            else:
                self.withdraw()
                print("Fail")
                print(f"current balance: {self.money}")
                print(f"current: {self.iPhones[self.current][0]}")

    def advance(self):
        self.current += 1 #self.iPhones[n+1]
    
    def withdraw(self):
        if self.current == 0:
            return
        else:
            self.current -= 1 #self.iPhones[n-1]
    
    def initialize(self):
        self.current = 0
        print("Restarted")
        print(f"current: {self.iPhones[self.current][0]}")
        print(f"chance: {self.iPhones[self.current][2] * 100}%")
        print(f"current balance: {self.money}")
        print(f"number of protections: {self.protection}")
        
    

if __name__ == "__main__":
    App = Iphone_Reinforcement()
    
    App.initialize()
    
    while True:
        command = str(input())
        if command == "ir close":
            sys.exit(0)
        else:
            App.Commanding(command)
