import sys
import tkinter as tk

def Protection(app, sub_4):
    app.protection += 1
    sub_4["text"] = f"Protection (current value: {app.protection})"

def Store(App):
    global protection_btn
    store = tk.Tk()
    store.title("iPhone Reinforcement - Store")
    store.resizable(width=False, height=False)
    store.geometry("500x400")
    store_lbl = tk.Label(text="BUY ANYTHING").pack()
    protection_lbl = tk.Label(text=f"protection value:{App.protection}")
    protection_btn = tk.Button(text=f"Protection (current value: {App.protection})", command=Protection(App, protection_lbl)).pack()
    exit_btn = tk.Button(text="exit store", command=store.quit()).pack()
    
    
    store.mainloop()
    
def Exit():
    sys.exit