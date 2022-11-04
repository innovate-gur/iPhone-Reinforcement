import sys
import random

class Iphone_Reinforcement(object):
    def __init__(self):
        self.iPhones = [
            ["iPhone", "June 29, 2007", 1],
            ["iPhone 3G", "July 11, 2008", 0.5],
            ["iPhone 3GS", "June 19, 2009", 0],
            ["iPhone 4", "June 24, 2010"],
            ["iPhone 4S", "October 14, 2011"],
            ["iPhone 5", "September 21, 2012"],
            ["iPhone 5S", "September 20, 2013"],
            ["iPhone 5C",  "September 20, 2013"],
            ["iPhone 6 ", "September 19, 2014"],
            ["iPhone 6 Plus", "September 19, 2014"],
            ["iPhone 6S", "September 19, 2015"],
            ["iPhone 6s Plus"],
            ["iPhone SE", "March 31, 2016"],
            ["iPhone 7 ", "September 16, 2016"],
            ["iPhone 7 Plus", "September 16, 2016"],
            ["iPhone 8 ", "September 22, 2017"],
            ["iPhone 8 Plus", "September 22, 2017"],
            ["iPhone X:", "November 3, 2017"],
            ["iPhone XS","September 21, 2018"],
            ["iPhone XS Max", "September 21, 2018"],
            ["iPhone XR", "October 26, 2018"],
            ["iPhone 11", "September 20, 2019"],
            ["iPhone 11 Pro", "September 20, 2019"],
            ["iPhone 11 Pro Max", "September 20, 2019"],
            ["iPhone 12", "October 23, 2020"],
            ["iPhone 12 Mini", "October 23, 2020"],
            ["iPhone 12 Pro", "October 23, 2020"],
            ["iPhone 12 Pro Max", "October 23, 2020"],
            ["iPhone 13", "September 14, 2021"],
            ["iPhone 13 Mini", "September 14, 2021"],
            ["iPhone 13 Pro", "September 14, 2021"],
            ["iPhone 13 Pro Max", "September 14, 2021"],
            ["iPhone 14", "September 16, 2022"],
            ["iPhone 14 Plus", "September 16, 2022"],
            ["iPhone 14 Pro", "September 16, 2022"],
            ["iPhone 14 Pro Max", "September 16, 2022"]
        ]
        self.current = 0  #self.iPhones[0]

    def Commanding(self, comm):
        command = comm
        if command[0:2] == "ir":
            var = command[3:]
            if var == "go":
                self.random_go(self.iPhones[self.current][2])
                print(f"chance: {self.iPhones[self.current][2] * 100}%")
            if var == "exit":
                self.current = 0
                return print("restart")
                        
        else:
            self.error(f"Command not found: {command[0:2]}")

    def error(self, msg: str):
        print(msg)
        
    def random_go(self, percentage: int):
        if random.random() <= percentage:
            self.advance()
            print("Succed")
            return print(f"current: {self.iPhones[self.current][0]}")
        else:
            self.withdraw()
            print("Fail")
            return print(f"current: {self.iPhones[self.current][0]}")
        
    def advance(self):
        self.current += 1 #self.iPhones[n+1]
    
    def withdraw(self):
        if self.current == 0:
            return
        else:
            self.current -= 1 #self.iPhones[n-1]
    
    

if __name__ == "__main__":
    App = Iphone_Reinforcement()
    
    #Initialize
    print(f"current: {App.iPhones[App.current][0]}")
    print(f"chance: {App.iPhones[App.current][2] * 100}%")
    
    while True:
        command = str(input())
        if command == "ir close":
            sys.exit(0)
        else:
            App.Commanding(command)
