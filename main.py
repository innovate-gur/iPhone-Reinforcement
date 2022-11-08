import tkinter as tk
from game.game import Iphone_Reinforcement
import sys

Win = tk.Tk()
Win.title("iPhone Reinforcement")
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
    
reinforce_btn = tk.Button(text="Reinforce", width=10, height=5, command=onClick_reinforce) 
sell_btn = tk.Button(text="sell", width=10, height=5, command=onClick_sell)
main_lbl = tk.Label(text="Main") #current iPhone STORE
sub_lbl = tk.Label(text="Sub") #percentage
sub_2_lbl = tk.Label(text="Sub2") #Succeed, Faild
sub_3_lbl = tk.Label(text="Sub3") #current money
App = Iphone_Reinforcement()
App.initialize(main_lbl, sub_lbl, sub_3_lbl)

main_lbl.pack()
sub_lbl.pack()
sub_2_lbl.pack()
sub_3_lbl.pack()
reinforce_btn.pack()
sell_btn.pack()

tk.mainloop()