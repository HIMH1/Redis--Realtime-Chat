# HIMH 31/3/2022
import threading
import redis  # Redis package for Python
import tkinter as tk

redis = redis.Redis(
    host='localhost',
    port=6379
)


def submit():
    msg = entry.get()
    redis.set(my_username + '_last', msg)  # Add data
    text.insert(tk.END, '\nYou: ' + msg)
    entry.delete(0, 'end')


my_username = 'Ali'
friend = 'Hassan'
window = tk.Tk()
entry = tk.Entry()
text = tk.Text()
submit = tk.Button(window, text='submit', command=submit)
last = ''


def get_msg():
    global last
    value = redis.get(str(friend + '_last'))  # Get data
    if value is not None:
        new = value.decode('utf-8')
        if new != last:
            text.insert(tk.END, '\n' + friend + ': ' + new)
            last = new
    threading.Timer(1, get_msg).start()


def start_chat():
    entry.pack()
    submit.pack()
    text.pack()
    window.mainloop()


if __name__ == '__main__':
    get_msg()
    start_chat()
