import tkinter as tk
import requests

DELAY = 2000
URL = "https://api.wazirx.com/api/v2/tickers"


def get_data(pair: str):
    pair = pair.lower()
    #print(pair)
    response = requests.get(URL)
    data = response.json()

    buy = (data[pair]['buy'])
    sell = (data[pair]['sell'])

    l1.config(text=f' Buy - {buy}\n Sell - {sell}')
    l1.after(DELAY, run)
    print(buy, sell)


root = tk.Tk()
root.title('WazirX Ticker API')
root.geometry('400x170')
root.resizable(0, 0)

l1 = tk.Label(root, text='')
l1.pack()

e1 = tk.Entry(root)
e1.pack()


def run():
    pair = str(e1.get())
    get_data(pair)


b1 = tk.Button(root, text='Update', command=run)
b2 = tk.Button(root, text='Close', command=exit)
b1.pack(padx=5, pady=5)
b2.pack(padx=5, pady=5)

root.mainloop()
