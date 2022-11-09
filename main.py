import tkinter as tk
from game.game import Iphone_Reinforcement

from store.store import Store
import sys

Win = tk.Tk()
Win.title("iPhone Reinforcement - Main")
Win.resizable(width=False, height=False)
Win.geometry("500x400")


'''
    if command == "sell":
        
        
    if command == "protection":
        App.protection_flag = True
    if command == "store":
        
        if store_command == "exit":
            ...
        if store_command == "protection":
            App.protection += 1
            print("purchased |protection|!")
'''
def onClick_reinforce():
    App.random_go(App.iPhones[App.current][2], main_lbl, sub_2_lbl, sub_3_lbl)
    sub_lbl["text"] = f"chance: {App.iPhones[App.current][2] * 100}%"
    
def onClick_store():
    
    print("Welcome to the store, but anything you want")
    print("|protection|: you can use this before you reinforce the iPhone and can protect you from Fails")
          
def onClick_sell():
    App.money += App.iPhones[App.current][3]
    App.initialize(main_lbl, sub_lbl, sub_3_lbl)

App = Iphone_Reinforcement()


reinforce_btn = tk.Button(text="Reinforce", width=10, height=5, command=onClick_reinforce) 
sell_btn = tk.Button(text="sell", width=10, height=5, command=onClick_sell)
main_lbl = tk.Label(text="Main") #current iPhone STORE
sub_lbl = tk.Label(text="Sub") #percentage
sub_2_lbl = tk.Label(text="Sub2") #Succeed, Faild
sub_3_lbl = tk.Label(text="Sub3") #current money
sub_4_lbl = tk.Label(text="Syb4") #protection
store_btn = tk.Button(text="Store", command=Store(App))


main_lbl.pack()
sub_lbl.pack()
sub_2_lbl.pack()
sub_3_lbl.pack()
sub_4_lbl.pack()
reinforce_btn.pack()
sell_btn.pack()
store_btn.pack()

App.initialize(main_lbl, sub_lbl, sub_3_lbl)

tk.mainloop()